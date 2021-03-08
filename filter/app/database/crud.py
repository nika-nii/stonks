from sqlalchemy import or_, and_
from sqlalchemy.orm import Session

from . import models
from . import schemas


def get_observer_for_user(db: Session, user_id: int):
    return db.query(models.Observers).filter(models.Observers.id == user_id).first()


def get_triggered_observers(db: Session, value: float, currency: str):
    return db.query(models.Observers)\
        .filter(models.Observers.currency == currency)\
        .filter(
            or_(
                and_(value > models.Observers.watch, models.Observers.event == 'up'),
                and_(value < models.Observers.watch, models.Observers.event == 'down')
            )
        )


def get_observers(db: Session):
    return db.query(models.Observers).all()


def create_observer(db: Session, observer: schemas.ObserverCreate):
    db_observers = models.Observers(user_id=observer.user_id, event=observer.event,
                                    watch=observer.watch, currency=observer.currency)
    db.add(db_observers)
    db.commit()
    db.refresh(db_observers)
    return db_observers