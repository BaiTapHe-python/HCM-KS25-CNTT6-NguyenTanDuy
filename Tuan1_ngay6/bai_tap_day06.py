from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class BookCreate(BaseModel):
    title: str
    author: str
    price: float
    pages: int

class BookResponse(BookCreate):
    id: int

books_db = []
book_id_counter = 1

book = {
    "title": "Dế Mèn Phiêu Lưu Ký",
    "author": "Tô Hoài",
    "price": 45000,
    "pages": 200
}

@app.post("/books", response_model=BookResponse)
def create_book(book: BookCreate):
    global book_id_counter

    new_book = {
        "id": book_id_counter,
        **book.model_dump()
    }

    books_db.append(new_book)
    book_id_counter += 1

    return new_book

@app.get("/books/{id}", response_model=BookResponse)
def get_book(id: int):
    for item in books_db:
        if item["id"] == id:
            return item

    raise HTTPException(
        status_code=404,
        detail="Book not found"
    )