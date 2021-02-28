from fastapi import FastAPI
from pydantic import BaseModel
import datetime

from email_notifier import EmailFactory

factory = EmailFactory()

user_getter = factory.user_getter
sender = factory.sender
formatter_builder = factory.formatter_builder()


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
    user_data = user_getter(notification.user_id)
    address = user_data.get_address()
    name = user_data.get_name()
    message = notification.message

    formatter_builder.set_currency(message.currency)
    formatter_builder.set_event(message.event)
    formatter_builder.set_name(name)
    formatter_builder.set_time(message.time)
    formatter_builder.set_value(message.value)
    formatter_builder.set_watch(message.watch)
    formatter = formatter_builder.get_formatter()

    message = formatter.render()
    sender(address).send(message)

    return notification
