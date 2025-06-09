from pydantic import BaseModel, Field
from datetime import datetime

class Documents_create(BaseModel):
    doc_date: datetime=Field(datetime.now().strftime("%Y-%m-%d"))
    title: str
    text: str

class Documents_update(BaseModel):
    doc_date: datetime=Field(datetime.now().strftime("%Y-%m-%d"))
    title: str
    text: str