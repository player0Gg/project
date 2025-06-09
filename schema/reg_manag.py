from pydantic import BaseModel

class Create_regmanag(BaseModel):
    title: str
    text: str
    full_name: str
    phone: int
    address: str

class Update_regmanag(BaseModel):
    title: str
    text: str
    full_name: str
    phone: int
    address: str