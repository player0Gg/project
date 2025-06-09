from sqlalchemy import Column, Integer, String, Text, DateTime
from db import Base

class Documents(Base):
    __tablename__="documents"
    id=Column(Integer, primary_key=True, index=True)
    doc_date=Column(DateTime, nullable=False)
    title=Column(Text, nullable=False)
    text=Column(Text, nullable=False)
    files_doc=Column(String, nullable=True)