from sqlalchemy import or_, and_
from sqlalchemy.orm import Session

from . import models, schemas


def get_observer_for_user(db: Session, user_id: int):
    return db.query(models.Observers).filter(models.Observers.id == user_id).all()


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


def create_observer(db: Session, observer: schemas.ObserverCreate, user_id: int):
    db_observer = models.Observers(**observer.dict(), user_id=user_id)
    db.add(db_observer)
    db.commit()
    db.refresh(db_observer)
    return db_observer