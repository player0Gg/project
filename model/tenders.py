from sqlalchemy import Column, Integer, String, Text
from db import Base

class Tender(Base):
    __tablename__ = "tenders"

    id=Column(Integer, primary_key=True, index=True)
    image=Column(String)
    text=Column(Text)
    files_tender=Column(String)
