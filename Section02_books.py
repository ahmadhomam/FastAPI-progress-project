from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self,id,title,author,description,rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating 


#creating a list of object of class Book
BOOK = [
    Book(1,"Wings of fire","Kalam sahab","Great inspiring book",4),
    Book(2,"Sacred nector","Safi ur rahman","Inspirational book",5),
    Book(3,"Half girlfriend","chetan bhagat","Romantic book",2),
    Book(4,"Harry potter","J.K rowling","True fantasy",4),
    Book(5,"Game of thrones","George R.R martin","Best fantasy book ever",5)
]

#validation using pydantic
class valid_book(BaseModel) :
    id: Optional[int]= None
    title: str = Field(min_length=3)
    author: str= Field(min_length=3, max_length=10)
    description: str= Field(max_length= 20)
    rating: int=  Field(gt=-1,lt=6)



@app.get("/books/")
async def read_list():
    return BOOK


@app.post("/books/")
async def create_valid(valid_var:valid_book):
    new_book = Book(**valid_var.model_dump())
    print(type(new_book))
    BOOK.append(assign_id(new_book))

#function to add id in cronologival order .
def assign_id(book:Book):
    book.id = 1 if len(BOOK) == 0 else BOOK[-1].id + 1
    return book