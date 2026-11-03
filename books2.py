from typing import Optional
from fastapi import FastAPI,Body,Path, Query, HTTPException
from pydantic import BaseModel, Field
from starlette import status

app = FastAPI()

class Book:
    id: int
    type:str
    author:str
    description:str
    rating:float
    price:float
    publish_date:int

    def __init__(self,id,type,author,description,rating,price,publish_date):
        self.id = id
        self.type = type
        self.author = author
        self.description = description
        self.rating = rating
        self.price = price
        self.publish_date = publish_date

class BookRequest(BaseModel):
    id: Optional[int] = Field(description="ID is not required", default=None)
    type:str = Field(min_length=3)
    author:str = Field(min_length=1)
    description:str = Field(min_length=1, max_length=100)
    rating:float= Field(gt=0,lt=6)
    price:float
    publish_date:int

    model_config = {
        "json_schema_extra":{
            "example":{
                "type": "Romance",
                "author": "Romeo",
                "description": "French Biryani",
                "rating": 3.34,
                "price": 105,
                "publish_date":2017
            }
        }
    }

BOOKS = [
    Book(1,'Science','Chad trevor','Astronomi',4.68,50,2022),
    Book(2,'Romance','Romeo','French kiss',3.34,105,2011),
    Book(4,'Literature','Galileo','Catestrophe',4.38,35,2017),
    Book(6,'Action','JK Rowling','HarryPotter',4.98,90,2023)
]

@app.get("/books",status_code=status.HTTP_200_OK)
async def read_books():
    return BOOKS

@app.get("/book/{book_id}",status_code=status.HTTP_200_OK)
async def get_book(book_id:int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book

    raise HTTPException(status_code=404, detail="Book not found")

@app.get("/book/rating/",status_code=status.HTTP_200_OK)
async def get_books_by_rating(book_rating: int = Query(gt=0,lt=6)):
    books_to_return = []
    for book in BOOKS:
        if book.rating <= book_rating:
            books_to_return.append(book)
    return books_to_return



@app.put("/book/update_book/",status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book: BookRequest):
    book_updated = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book
            book_updated = True

    if not book_updated:
        raise HTTPException(status_code=404, detail="Book not found")

@app.post("/new-book",status_code=status.HTTP_201_CREATED)
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

@app.delete("/book/{book_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int = Path(gt=0)):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            break