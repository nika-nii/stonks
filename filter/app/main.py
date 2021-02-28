from fastapi import FastAPI, requests, Depends
from pydantic import BaseModel
from database.database import engine, SessionLocal
from database import models
from sqlalchemy.orm import Session
from database.models import Observers
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


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


models.Base.metadata.create_all(bind=engine)


@app.post("/add")
async def send_value(message: Message):
    return message


@app.post("/watch")
async def add_observer(observer: Observer):
    return observer


@app.get("/watch")
async def get_observers_list(db: Session = Depends(get_db()), skip: int = 0, limit: int = 100):
    #должна быть подключена БД, должны возвращаться данные из нее
    return db.query(models.Item).offset(skip).limit(limit).all()


@app.get("/watch/{id}")
async def observer():
    #после созадния бд нужно реализовать логику
    #по указанному id обращаемся к бд, берем из нее observer-а и возвращаем его
    return 'work in progress'
