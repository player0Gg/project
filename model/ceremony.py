from sqlalchemy import Column, Integer, String, DateTime, Text
from db import Base

class Ceremony(Base):
    __tablename__ = "ceremony"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    text = Column(Text)
    date = Column(DateTime)
    image = Column(String)  # Optional image field