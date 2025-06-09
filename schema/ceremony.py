from pydantic import BaseModel, Field
from datetime import datetime

class Ceremony_create(BaseModel):
    title: str
    text: str
    date: str=Field(datetime.now())

class Ceremony_update(BaseModel):
    title: str
    text: str
    date: str=Field(datetime.now())

