from pydantic import BaseModel
from typing import List, Optional

class BookBase(BaseModel):
    title: str
    author_id: str

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: Optional[str]

    class Config:
        orm_mode = True

class AuthorBase(BaseModel):
    name: str

class AuthorCreate(AuthorBase):
    pass

class Author(AuthorBase):
    id: Optional[str]
    books: List[Book] = []

    class Config:
        orm_mode = True
