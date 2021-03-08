import datetime
import json
import os

import schedule

import requests

from dotenv import load_dotenv
# Загружаем параметры
load_dotenv()

period = int(os.getenv('PERIOD_SECS'))

def get_data_from_api():
    print("I'm working...")
    r = requests.get(FOREIGN_API)
    data = r.json()
    rates = data['rates']
    date = datetime.strptime(rates['date'], "%Y-%m-%d")
    for rate in rates.keys():
        message = {
            "value": rates[rate],
            "currency": rate,
            "time": date
        }
        requests.post(
            os.getenv(STORAGE_API),
            data=json.dumps(message, default=str)
        )

schedule.every(period).seconds.do(get_data_from_api)
