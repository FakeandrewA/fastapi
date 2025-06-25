from typing import Optional
from pydantic import BaseModel

class BaseProduct(BaseModel):
    name: str
    price: int

class CreateProduct(BaseProduct):
    pass 
class UpdateProduct(BaseProduct):
    pass 
