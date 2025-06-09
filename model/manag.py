from sqlalchemy import Column, Integer, String, JSON, Text
from db import Base

class Manag(Base):
    __tablename__='management'
    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String)
    phone_number = Column(String)
    position = Column(String)
    image = Column(String)
    free_day = Column(String)
    about = Column(Text)
    author = Column(JSON)