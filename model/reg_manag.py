from sqlalchemy import Column, Integer, String, Text
from db import Base

class Reg_manag(Base):
    __tablename__="region_management"
    id=Column(Integer, primary_key=True, index=True)
    image=Column(String,nullable=True)
    title=Column(Text,nullable=False)
    text=Column(Text,nullable=False)
    full_name=Column(String,nullable=False)
    phone=Column(Integer,nullable=False)
    address=Column(String,nullable=False)