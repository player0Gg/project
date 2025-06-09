from pydantic import BaseModel, Field
from datetime import datetime

class Event_create(BaseModel):
    title: str
    text: str
    date: str=Field(datetime.now())

class Event_update(BaseModel):
    title: str
    text: str
    date: str=Field(datetime.now())