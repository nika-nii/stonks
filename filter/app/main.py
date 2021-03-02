from fastapi import FastAPI, requests, Depends, HTTPException
from pydantic import BaseModel
from database.database import engine, SessionLocal
from sqlalchemy.orm import Session
from database import crud, models
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
async def get_observers_list(db: Session = Depends(get_db)):
    #должна быть подключена БД, должны возвращаться данные из нее
    db = crud.get_observers(db)
    if db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db


@app.get("/watch/{id}")
async def observer():
    #после созадния бд нужно реализовать логику
    #по указанному id обращаемся к бд, берем из нее observer-а и возвращаем его
    return 'work in progress'
