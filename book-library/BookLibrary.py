from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Book(BaseModel):
    title: str
    author: str
    year: str
    id:int

#database with a list
booksDB: List[Book] = []
book_id_counter = 1



@app.post("/books/")
async def add_Book(title:str,author:str,year:str):
    global book_id_counter
    
    # Create the book instance with an assigned id
    created_book = Book(
        id=book_id_counter,
        title=title,
        author=author,
        year=year
    )

    book_id_counter +=1

    booksDB.append(created_book)
    booksDB

    return created_book


@app.get("/books/")
async def get_all_books():
    
    return booksDB

@app.get("/books/{id}")
async def get_book_by_id(id:int):
    
    for book in booksDB:
     
        if book.id == id:
    
            return book
        
@app.put("/books/{id}")
async def update_book(id: int, new_title:str, new_author:str, new_year:str):
    
    for book in booksDB:
        
        if book.id == id:
            
            book.title = new_title
            book.author = new_author
            book.year = new_year
    
            return book
        
@app.delete("/books/{id}")
async def delete_book(id:int):
    
    for index, book in enumerate(booksDB):
    
        if book.id == id:
    
            booksDB.pop(index)

        

