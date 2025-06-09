from sqlalchemy import Column, Integer, String, Text
from db import Base

class Reg_manag(Base):
    __tablename__="region_management"
    id=Column(Integer, primary_key=True, index=True)
    image=Column(String)
    title=Column(String)
    text=Column(Text)
    full_name=Column(String)
    phone=Column(Integer)
    address=Column(String)