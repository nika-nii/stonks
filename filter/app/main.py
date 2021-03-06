import datetime
import json

import requests
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database import crud, models
from database.database import engine, SessionLocal


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
async def send_value(message: Message, db: Session = Depends(get_db)):
    db = crud.get_triggered_observers(db, message.value, message.currency)
    for observer in db:
        notification = {
            "user_id": observer.user_id,
            "message": {
                "event": observer.event,
                "watch": observer.watch,
                "value": message.value,
                "time": message.time,
                "currency": message.currency
            }
        }
        r = requests.post('http://localhost:80/notify', data=json.dumps(notification, default=str))
        print(r)
    return "OK"


@app.post("/watch")
async def add_observer(observer: Observer, db: Session = Depends(get_db)):
    db = crud.create_observer(db, observer)
    return db


@app.get("/watch")
async def get_observers_list(db: Session = Depends(get_db)):
    # должна быть подключена БД, должны возвращаться данные из нее
    db = crud.get_observers(db)
    if db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db


@app.get("/watch/{id}")
async def observer(id, db: Session = Depends(get_db)):
    # после созадния бд нужно реализовать логику
    # по указанному id обращаемся к бд, берем из нее observer-а и возвращаем его
    db = crud.get_observer_for_user(db, user_id=id)
    if db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db
