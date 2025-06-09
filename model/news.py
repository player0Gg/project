from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.orm import relationship
from db import Base

class News(Base):
    __tablename__ = 'news'
    id=Column(Integer, primary_key=True, index=True)
    image=Column(String)
    create_at=Column(DateTime)
    title=Column(String)
    description=Column(Text)
    text=Column(Text)    
