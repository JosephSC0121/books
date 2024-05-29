from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from motor.motor_asyncio import AsyncIOMotorClient
from models import AuthorInDB, BookInDB
from schemas import AuthorCreate, Author, BookCreate, Book
from database import get_database

app = FastAPI()

# Configuración de CORS
origins = [
    "http://localhost:3000",  # React frontend
    "http://127.0.0.1:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/authors/", response_model=Author)
async def create_author(author: AuthorCreate, db: AsyncIOMotorClient = Depends(get_database)):
    db_author = AuthorInDB(**author.dict())
    result = await db["authors"].insert_one(db_author.dict())
    db_author.id = str(result.inserted_id)
    return db_author

@app.get("/authors/", response_model=List[Author])
async def read_authors(db: AsyncIOMotorClient = Depends(get_database)):
    authors = await db["authors"].find().to_list(1000)
    return [Author(**author) for author in authors]

@app.get("/authors/{author_id}", response_model=Author)
async def read_author(author_id: str, db: AsyncIOMotorClient = Depends(get_database)):
    author = await db["authors"].find_one({"_id": author_id})
    if author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return Author(**author)

@app.put("/authors/{author_id}", response_model=Author)
async def update_author(author_id: str, author: AuthorCreate, db: AsyncIOMotorClient = Depends(get_database)):
    result = await db["authors"].update_one({"_id": author_id}, {"$set": author.dict()})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Author not found")
    updated_author = await db["authors"].find_one({"_id": author_id})
    return Author(**updated_author)

@app.delete("/authors/{author_id}")
async def delete_author(author_id: str, db: AsyncIOMotorClient = Depends(get_database)):
    result = await db["authors"].delete_one({"_id": author_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Author not found")
    return {"message": "Author deleted"}

@app.post("/books/", response_model=Book)
async def create_book(book: BookCreate, db: AsyncIOMotorClient = Depends(get_database)):
    db_book = BookInDB(**book.dict())
    result = await db["books"].insert_one(db_book.dict())
    db_book.id = str(result.inserted_id)
    return db_book

@app.get("/books/", response_model=List[Book])
async def read_books(db: AsyncIOMotorClient = Depends(get_database)):
    books = await db["books"].find().to_list(1000)
    return [Book(**book) for book in books]

@app.get("/books/{book_id}", response_model=Book)
async def read_book(book_id: str, db: AsyncIOMotorClient = Depends(get_database)):
    book = await db["books"].find_one({"_id": book_id})
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return Book(**book)

@app.put("/books/{book_id}", response_model=Book)
async def update_book(book_id: str, book: BookCreate, db: AsyncIOMotorClient = Depends(get_database)):
    result = await db["books"].update_one({"_id": book_id}, {"$set": book.dict()})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Book not found")
    updated_book = await db["books"].find_one({"_id": book_id})
    return Book(**updated_book)

@app.delete("/books/{book_id}")
async def delete_book(book_id: str, db: AsyncIOMotorClient = Depends(get_database)):
    result = await db["books"].delete_one({"_id": book_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted"}
