from sqlalchemy import Column, Integer, String, Text, DateTime
from db import Base

class Documents(Base):
    __tablename__="documents"
    id=Column(Integer, primary_key=True, index=True)
    doc_date=Column(DateTime)
    title=Column(Text)
    text=Column(Text)
    files_doc=Column(String)