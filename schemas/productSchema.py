from doctest import debug_script
from typing import Optional
from pydantic import BaseModel

class Product(BaseModel):
    id :Optional[str]
    name : str
    description : Optional[str]

class CreateProduct(BaseModel):
    name: str
    description : str

class MessageError(BaseModel):
    code : str
    message: str