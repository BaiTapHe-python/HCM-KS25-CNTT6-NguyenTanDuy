from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from database import get_db, engine, Base
from models import BookModel
from schemas import BookCreate

app = FastAPI(title="Library Management MySQL")

Base.metadata.create_all(bind=engine)

@app.post("/books", status_code=status.HTTP_201_CREATED)
def add_book(book: BookCreate, db: Session = Depends(get_db)):
    new_book = BookModel(**book.model_dump())
    try:
        db.add(new_book)
        db.commit()
        db.refresh(new_book)
        return {
            "id": new_book.id,
            "code": new_book.code,
            "title": new_book.title,
            "price": float(new_book.price),
            "pages": new_book.pages
        }
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Mã sách đã tồn tại!")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/books", status_code=status.HTTP_200_OK)
def get_all_books(db: Session = Depends(get_db)):
    books = db.query(BookModel).all()
    return [
        {
            "id": b.id,
            "code": b.code,
            "title": b.title,
            "price": float(b.price),
            "pages": b.pages
        }
        for b in books
    ]