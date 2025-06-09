from pydantic import BaseModel, json

class Manag_create(BaseModel):
    full_name: str
    phone_number: int
    position: str
    image: str
    free_day: str
    about: str
    author: str

class Manag_update(BaseModel):
    full_name: str
    phone_number: int
    position: str
    image: str
    free_day: str
    about: str
    author: str