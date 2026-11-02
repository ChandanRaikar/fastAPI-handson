from typing import Optional
from fastapi import FastAPI,Body
from pydantic import BaseModel, Field
from pydantic_core.core_schema import json_schema

app = FastAPI()

class Book:
    id: int
    type:str
    author:str
    description:str
    rating:float
    price:float

    def __init__(self,id,type,author,description,rating,price):
        self.id = id
        self.type = type
        self.author = author
        self.description = description
        self.rating = rating
        self.price = price

class BookRequest(BaseModel):
    id: Optional[int] = Field(description="ID is not required", default=None)
    type:str = Field(min_length=3)
    author:str = Field(min_length=1)
    description:str = Field(min_length=1, max_length=100)
    rating:float= Field(gt=0,lt=6)
    price:float

    model_config = {
        "json_schema_extra":{
            "example":{ 
                "type": "Romance",
                "author": "Romeo",
                "description": "French kiss",
                "rating": 3.34,
                "price": 105
            }
        }
    }

BOOKS = [
    Book(1,'Science','Chad trevor','Astronomi','4.68','50'),
    Book(2,'Romance','Romeo','French kiss','3.34','105'),
    Book(4,'Literature','Galileo','Catestrophe','4.38','35'),
    Book(6,'Action','JK Rowling','HarryPotter','4.98','90')
]

@app.get("/")
async def read_books():
    return BOOKS


@app.post("/new-book")
async def create_book(book_request:BookRequest):
    new_book = Book(**book_request.model_dump())
    print(new_book)
    BOOKS.append(find_book_id(new_book))

def find_book_id(book:Book):
    if len(BOOKS)>0:
        book.id = BOOKS[-1].id +1
    else:
        book.id = 1
    return book