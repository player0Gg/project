from pydantic import BaseModel, Field

class User_create(BaseModel):
    name: str
    username: str
    email: str
    password: str

class User_update(BaseModel):
    name:str
    username:str
    email:str
    password:str

class Admin_create(BaseModel):
    name: str
    username: str
    email: str
    password: str
    role: str

class Admin_update(BaseModel):
    name: str
    username: str
    email: str
    password: str
    role: str