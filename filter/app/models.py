from sqlalchemy import Column, Integer, String

from database import Base


class Observers(Base):
    __tablename__ = "observers"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    event = Column(String)
    watch = Column(Integer)
    currency = Column(String)