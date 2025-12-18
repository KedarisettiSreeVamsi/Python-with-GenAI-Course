from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True

product1 = Product(id=1,name="Laptop",price=1599.99,in_stock=True)
product2 = Product(id=2,name="Mouse",price=24.59)
product3= Product(name="Keyboard")
