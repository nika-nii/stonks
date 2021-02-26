from fastapi import FastAPI
from pydantic import BaseModel
import datetime

class Message(BaseModel):
	event: str
	watch: float
	value: float
	time: datetime.datetime
	currency: str


class Notification(BaseModel):
    user_id: int
    message: Message


app = FastAPI()


@app.post("/notify")
async def create_notification(notification: Notification):
    return notification
