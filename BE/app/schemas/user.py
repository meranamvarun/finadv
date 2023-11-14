from pydantic import BaseModel
from typing import List


class UserBase(BaseModel):
    username: str
    email: str
    contact_number: str
    comm_address: str
    home_address: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    investments: List['Investment'] = []

    class Config:
        orm_mode = True
