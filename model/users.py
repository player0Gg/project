from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db import Base

class Users(Base):
    __tablename__ = 'users'
    id=Column(Integer, primary_key=True, index=True)
    name=Column(String)
    username=Column(String)
    email=Column(String)
    password=Column(String)
    token=Column(String, nullable=True)  # Nullable token for users without a token
    role=Column(String)