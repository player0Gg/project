from pydantic import BaseModel, Field
from datetime import datetime

class News_create(BaseModel):
    create_at: datetime = Field(default_factory=datetime.now)
    title: str
    description: str
    text: str

class News_update(BaseModel):
    create_at: datetime = Field(default_factory=datetime.now)
    title: str
    description: str
    text: str