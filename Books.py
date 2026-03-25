from fastapi import FastAPI     # importing the dependencies FastAPI from fastapi directory

app = FastAPI()                 # help the uvicorn(surver) to identify this application is FastAPI


books = [
    {"title": "Spider man","Author": "Stan Lee", "category": "Comics"},
    {"title": "Amazing Spider man","Author": "Stan Lee", "category": "Comics"},
    {"title": "Harry Potter one","Author": "J.K Rowling", "category": "Comics"},
    {"title": "Harry Potter two","Author": "J.K Rowling", "category": "Comics"},
    {"title": "Half Girlfriend","Author": "Chetan Bagat", "category": "Romantic"},
]

#path paramter
@app.get("/books/")
async def read_books() :         # python function 
    return books


#dyamic parameter
@app.get("/books/{title_name}")
async def read_books(title_name:str) :         # python function 
    for book in books:
        if book.get("title").casefold() == title_name.casefold() :
            return book

#query parameter

@app.get("/{book_title}/")
async def book_for_query(book_title:str,category:str) :
    book_to_show = []
    for book in books:
        if (book.get("title").casefold() == book_title.casefold() and 
            book.get("category").casefold() == category.casefold()):
            book_to_show.append(book)
    
    return book_to_show