from sqlalchemy import Column, Integer, String, DateTime
from db import Base

class Event(Base):
    __tablename__ = 'events'

    id=Column(Integer, primary_key=True, index=True)
    title=Column(String)
    text=Column(String)
    date=Column(DateTime)