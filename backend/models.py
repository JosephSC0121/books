from pydantic import BaseModel, Field
from typing import List, Optional

class AuthorInDB(BaseModel):
    id: Optional[str] = Field(alias="_id")
    name: str

class BookInDB(BaseModel):
    id: Optional[str] = Field(alias="_id")
    title: str
    author_id: str
