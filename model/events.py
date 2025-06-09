from sqlalchemy import Column, Integer, Text, DateTime
from db import Base

class Event(Base):
    __tablename__ = 'events'

    id=Column(Integer, primary_key=True, index=True)
    title=Column(Text,nullable=False)
    text=Column(Text,nullable=False)
    date=Column(DateTime,nullable=False)