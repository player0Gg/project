from sqlalchemy import Column, Integer, String, JSON, Text
from db import Base

class Manag(Base):
    __tablename__='management'
    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String,nullable=False)
    phone_number = Column(String,nullable=False)
    position = Column(String,nullable=False)
    image = Column(String,nullable=True)
    free_day = Column(String,nullable=False)
    about = Column(Text,nullable=False)
    author = Column(JSON,nullable=False)