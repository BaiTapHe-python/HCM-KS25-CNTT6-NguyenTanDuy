from pydantic import BaseModel

class BookCreate(BaseModel):
    code: str
    title: str
    price: float
    pages: int