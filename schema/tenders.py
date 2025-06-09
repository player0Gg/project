from pydantic import BaseModel, Field

class Tender_create(BaseModel):
    text: str

class Tender_update(BaseModel):
    text: str