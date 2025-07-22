from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Book(BaseModel):
    title: str
    author: str
    pages: str
    published: bool

books = []


@app.get("/")
def hello():
    return {"message": "本の管理APIです"}

@app.get("/books")
def get_books():
    return books

@app.post("/books")
def add_book(book: Book):
    books.append(book)
    return {"message": "本を追加しました", "book": book}


@app.get("/books/{book_id}")
def get_book(book_id: int):
    if book_id < 0 or book_id >= len(books):
        raise HTTPException(status_code=404, detail= "本が見つかりません")
    return books[book_id]

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    if book_id < 0 or book_id >= len(books):
        raise HTTPException(status_code=404, detail= "本が見つかりません")
    delete_book = books.pop(book_id)
    return {"message": "本を削除しました", "deleted_book": delete_book}



