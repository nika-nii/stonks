from fastapi import FastAPI
from pydantic import BaseModel
import datetime

class Message(BaseModel):
	time: datetime.datetime
	value: float
	currency: str


class Observer(BaseModel):
    id: int
    user_id: int
    event: str
    watch: int
    currency: str

app = FastAPI()


@app.post("/add")
async def send_value(message: Message):
    return message

@app.post("/watch")
async def add_observer(observer: Observer):
    return observer

@app.get("/watch")
async def get_observers_list():
    #должна быть подключена БД, должны возвращаться данные из нее
    return 'work in progress'

@app.get("/watch/{id}")
async def observer():
    #после созадния бд нужно реализовать логику
    #по указанному id обращаемся к бд, берем из нее observer-а и возвращаем его
    return 'work in progress'
