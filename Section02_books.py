from fastapi import FastAPI,Body
from pydantic import BaseModel

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
    id: int
    title: str
    author: str
    description: str
    rating: int



@app.get("/books/")
async def read_list():
    return BOOK


@app.post("/books/")
async def create_valid(valid_var:valid_book):
    new_book = Book(**valid_var.model_dump())
    print(type(new_book))
    BOOK.append(new_book)