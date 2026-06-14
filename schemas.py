from pydantic import BaseModel
from datetime import datetime
from typing import Optional

#----------Product Schema------------#

class ProductCreate(BaseModel):
    name: str
    price: float
    stock: int = 0

class ProductUpdate(BaseModel):
    name: Optional[str]= None
    price: Optional[float] = None
    stock: Optional[int]= None

class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    stock: int
    created_at: datetime

    model_config = {"from_attributes": True}

#----------USER SCHEMA-----------------#

class UserCreate(BaseModel):
    username: str
    email: str
    password: str       

class UserUpdate(BaseModel):
    username: Optional[str]= None
    email: Optional[str]= None


class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    created_at: datetime

    model_config = {"from_attributes": True} 