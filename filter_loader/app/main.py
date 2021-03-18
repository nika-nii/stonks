import schedule
import requests
import time
import os
import json

from dotenv import load_dotenv
# Загружаем параметры
load_dotenv()

host1 = "http://storage/"
host2 = "http://filter/add"

def job():
    r = requests.get(f'{host1}currencies')
    for cur in r.json():
        r = requests.get(f'{host1}latest/{cur}')
        data = r.json()
        data['currency'] = cur
        requests.post(
            host2,
            data=json.dumps(data, default=str)
        )

schedule.every(60).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)