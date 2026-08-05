from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Book(BaseModel):
    id: int
    ten_sach: str
    tac_gia: str
    nam_xuat_ban: int
    so_luong: int

danh_sach_sach = [
    {
        "id": 1,
        "ten_sach": "Nhà Giả Kim",
        "tac_gia": "Paulo Coelho",
        "nam_xuat_ban": 1988,
        "so_luong": 5
    },
    {
        "id": 2,
        "ten_sach": "Dế Mèn Phiêu Lưu Ký",
        "tac_gia": "Tô Hoài",
        "nam_xuat_ban": 1941,
        "so_luong": 8
    },
    {
        "id": 3,
        "ten_sach": "Lão Hạc",
        "tac_gia": "Nam Cao",
        "nam_xuat_ban": 1943,
        "so_luong": 6
    }
]

@app.post("/api/v1/books", response_model=Book)
def create_book(book: Book):
    danh_sach_sach.append(book.model_dump())
    return book

@app.get("/api/v1/books", response_model=list[Book])
def get_all_books():
    return danh_sach_sach

@app.get("/api/v1/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    for book in danh_sach_sach:
        if book["id"] == book_id:
            return book
    raise HTTPException(
        status_code=404,
        detail=f"Không tìm thấy sách với id: {book_id}"
    )

@app.put("/api/v1/books/{book_id}", response_model=Book)
def update_book(book_id: int, new_book: Book):
    for i in range(len(danh_sach_sach)):
        if danh_sach_sach[i]["id"] == book_id:
            danh_sach_sach[i] = new_book.model_dump()
            return danh_sach_sach[i]
    raise HTTPException(
        status_code=404,
        detail=f"Không tìm thấy sách với id: {book_id}"
    )

@app.delete("/api/v1/books/{book_id}", response_model=Book)
def delete_book(book_id: int):
    for i in range(len(danh_sach_sach)):
        if danh_sach_sach[i]["id"] == book_id:
            return danh_sach_sach.pop(i)
    raise HTTPException(
        status_code=404,
        detail=f"Không tìm thấy sách với id: {book_id}"
    )