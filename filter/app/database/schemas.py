from typing import List, Optional

from pydantic import BaseModel


class ObserverBase(BaseModel):
    user_id: int
    event: str
    watch: int
    currency: str


class ObserverCreate(ObserverBase):
    pass


class Observer(ObserverBase):
    id: int

    class Config:
        orm_mode = True