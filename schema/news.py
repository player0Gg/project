from pydantic import BaseModel, Field
from datetime import datetime

class News_create(BaseModel):
    create_at: str
    title: str
    description: str=Field(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    text: str

class News_update(BaseModel):
    create_at: str
    title: str
    description: str=Field(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    text: str