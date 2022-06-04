from lib2to3.pytree import Base
from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    id: Optional[str]
    name: str
    email: str
    password: str

class UserUpdateName(BaseModel):
    name: str

class UserUpdatePassword(BaseModel):
    password: str