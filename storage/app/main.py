from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

import os

from dotenv import load_dotenv
load_dotenv()


from datetime import datetime

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

token = os.getenv('INFLUX_TOKEN')
org = os.getenv('INFLUX_ORG')
bucket = os.getenv('INFLUX_BUCKET')
host = os.getenv('INFLUX_HOST')
port = os.getenv('INFLUX_PORT')

client = InfluxDBClient(url=f"http://{host}:{port}", token=token, org=org)
write_api = client.write_api(write_options=SYNCHRONOUS)
query_api = client.query_api()


class Value(BaseModel):
    time: datetime
    value: float
    currency: str

class TimeValue(BaseModel):
    time: datetime
    value: float


app = FastAPI()


@app.post("/add")
async def add_value(value: Value):
    data = Point("exchange").tag("currency", value.currency).field("value", value.value)
    write_api.write(bucket=bucket, record=data)
    return value


@app.get("/range/{currency}")
async def get_range(
    currency, 
    start: Optional[datetime] = None, 
    stop: Optional[datetime] = None
    ):
    print(start, type(start))
    print(stop, type(stop))
    range_start = f"start: {start.isoformat()}" if start else None
    range_stop = f"stop: {stop.isoformat()}" if stop else None
    range_part = ", ".join(
        filter(lambda x: x is not None, (range_start, range_stop, ))
    )
    filter_part = f' |> filter(fn: (r) => r["currency"] == "{currency}")'
    filter_part = ' |> filter(fn: (r) => r["_measurement"] == "exchange") |> filter(fn: (r) => r["_field"] == "value")' + filter_part
    range_part = f' |> range({range_part})' if range_part else " |> range(start: -1d)"
    query = f'from(bucket: "{bucket}"){range_part}{filter_part}'
    tables = query_api.query(query)

    results = []
    for table in tables:
        for record in table.records:
            results.append({"time": record.get_time(), "value": record.get_value()})
    return results


@app.get("/currencies")
async def get_currencies():
    query = '''import "influxdata/influxdb/schema"
               schema.measurementTagValues(bucket: "test", measurement: "exchange", tag: "currency")'''
    tables = query_api.query(query)

    results = []
    for table in tables:
        for record in table.records:
            results.append(record.get_value())
    return results


@app.get("/latest/{currency}")
async def get_latest(currency):
    query = f'''from(bucket: "{bucket}")
                        |> range(start: -1d)
                        |> filter(fn: (r) => r["currency"] == "{currency}")
                        |> filter(fn: (r) => r["_measurement"] == "exchange") 
                        |> filter(fn: (r) => r["_field"] == "value")
                        |> limit(n:1)'''
    tables = query_api.query(query)

    results = []
    for table in tables:
        for record in table.records:
            results.append({"time": record.get_time(), "value": record.get_value()})
    return results[0]