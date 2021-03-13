import schedule
import requests

from dotenv import load_dotenv
# Загружаем параметры
load_dotenv()

host1 = "http://storage/latest"
host2 = "http://filter/add"

def podskok():
    r = requests.get(host1)
    data = r.json()
    requests.post(
        os.getenv('STORAGE_API'),
        data=data
    )

schedule.every(10).seconds.do(podskok)

while True:
    schedule.run_pending()
    time.sleep(1)