from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.orm import relationship
from db import Base

class News(Base):
    __tablename__ = 'news'
    id=Column(Integer, primary_key=True, index=True)
    image=Column(String,nullable=True)
    create_at=Column(DateTime,nullable=False)
    title=Column(String,nullable=False)
    description=Column(Text,nullable=False)
    text=Column(Text,nullable=False)    
