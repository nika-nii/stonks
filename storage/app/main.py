from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

import os

from dotenv import load_dotenv
load_dotenv()


from datetime import datetime

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# You can generate a Token from the "Tokens Tab" in the UI
token = os.getenv('INFLUX_TOKEN')
org = os.getenv('INFLUX_ORG')
bucket = os.getenv('INFLUX_BUCKET')
host = os.getenv('INFLUX_HOST')
port = os.getenv('INFLUX_PORT')

client = InfluxDBClient(url=f"http://{host}:{port}", token=token)


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
    write_api = client.write_api(write_options=SYNCHRONOUS)
    data = Point("exchange").tag("currency", value.currency).field("value", value.value)
    write_api.write(bucket, org, data)
    return value

@app.get("/range/{currency}")
async def get_range(
    currency, 
    start: Optional[datetime] = None, 
    end: Optional[datetime] = None
    ):
    return "To be implemented"

@app.get("/currencies")
async def get_currencies():
    return "To be implemented"