from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Observers(Base):
    __tablename__ = "observers"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, unique=True, index=True)
    event = Column(String)
    watch = Column(Integer)
    currency = Column(String)