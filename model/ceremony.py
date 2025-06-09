from sqlalchemy import Column, Integer, String, DateTime, Text
from db import Base

class Ceremony(Base):
    __tablename__ = "ceremony"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(Text, nullable=False)
    text = Column(Text, nullable=False)
    date = Column(DateTime, nullable=False)
    image = Column(String, nullable=True)  # Optional image field