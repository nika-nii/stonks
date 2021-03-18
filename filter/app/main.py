import datetime
import json

import requests
from fastapi import FastAPI, Depends, HTTPException, Request
from pydantic import BaseModel
from sqlalchemy.orm import Session

import crud, models, schemas
from database import engine, SessionLocal

import os

from dotenv import load_dotenv
load_dotenv()

users_host = os.getenv('USERS_HOST')
notifier_host = os.getenv('NOTIFIER_HOST')

class Message(BaseModel):
    time: datetime.datetime
    value: float
    currency: str


# class Observer(BaseModel):
#     id: int
#     user_id: int
#     event: str
#     watch: int
#     currency: str

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


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
        r = requests.post(f'http://{notifier_host}/notify', data=json.dumps(notification, default=str))
        print(r)
    return "OK"


@app.post("/watch")
async def add_observer(observer: schemas.ObserverCreate, request: Request, db: Session = Depends(get_db)):
    token = request.headers['Authorization']
    print(token)
    headers = {
        'Authorization': token
    }
    r = requests.get(f'http://{users_host}/get_my_id')
    user_id = r.json()["id"]
    db = crud.create_observer(db, observer, user_id)
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
