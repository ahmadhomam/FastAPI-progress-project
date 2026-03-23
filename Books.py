from fastapi import FastAPI     # importing the dependencies FastAPI from fastapi directory

app = FastAPI()                 # help the uvicorn(surver) to identify this application is FastAPI


books = [
    {"title": "Spider_man","Author": "Stan Lee", "category": "Comics"},
    {"title": "Amazing Spider_man","Author": "Stan Lee", "category": "Comics"},
    {"title": "Harry Potter one","Author": "J.K Rowling", "category": "Comics"},
    {"title": "Harry Potter two","Author": "J.K Rowling", "category": "Comics"},
    {"title": "Half Girlfriend","Author": "Chetan Bagat", "category": "Romantic"},
]


@app.get("/books/{title_name}")
async def read_books(title_name:str) :         # python function 
    for book in books:
        if book.get("title").casefold() == title_name.casefold() :
            return book