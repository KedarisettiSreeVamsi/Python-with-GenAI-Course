from typing import List,Optional
from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class User(BaseModel):
    name: str
    address: Address


address = Address(street="123",city="Vizag",postal_code="530032")
user = User(name="Vamsi",address=address)