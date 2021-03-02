import datetime
import json
import os

import schedule

import requests


def get_data_from_api():
    print("I'm working...")
    r = requests.get('https://api.exchangeratesapi.io/latest')
    data = r.json()
    rates = data['rates']
    date = datetime.strptime(rates['date'], "%Y-%m-%d")
    for rate in rates.keys():
        message = {
            "value": rates[rate],
            "currency": rate,
            "time": date
        }
        requests.post(os.getenv('FOREIGN_API'), data=json.dumps(message, default=str))
        #заменить запрос в env


schedule.every().day.do(get_data_from_api)