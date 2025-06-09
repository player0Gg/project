from sqlalchemy import Column, Integer, String, Text
from db import Base

class Tender(Base):
    __tablename__ = "tenders"

    id=Column(Integer, primary_key=True, index=True)
    image=Column(String,nullable=True)
    text=Column(Text,nullable=False)
    files_tender=Column(String,nullable=True)
