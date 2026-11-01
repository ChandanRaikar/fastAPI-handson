from fastapi import FastAPI,Body

app = FastAPI()

BOOKS = books = [
    {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'Category': 'Classic Fiction'},
    {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'Category': 'Fiction'},
    {'title': '1984', 'author': 'George Orwell', 'Category': 'Dystopian Fiction'},
    {'title': 'The Alchemist', 'author': 'Paulo Coelho', 'Category': 'Adventure'},
    {'title': 'Pride and Prejudice', 'author': 'Jane Austen', 'Category': 'Romance'},
    {'title': 'The Hobbit', 'author': 'J.R.R. Tolkien', 'Category': 'Fantasy'},
    {'title': 'Harry Potter and the Philosopher\'s Stone', 'author': 'J.K. Rowling', 'Category': 'Fantasy'},
    {'title': 'The Catcher in the Rye', 'author': 'J.D. Salinger', 'Category': 'Fiction'},
    {'title': 'The Book Thief', 'author': 'Markus Zusak', 'Category': 'Historical Fiction'},
    {'title': 'The Da Vinci Code', 'author': 'Dan Brown', 'Category': 'Mystery'},
    {'title': 'Atomic Habits', 'author': 'James Clear', 'Category': 'Self-Help'},
    {'title': 'Rich Dad Poor Dad', 'author': 'Robert T. Kiyosaki', 'Category': 'Finance'},
    {'title': 'The Psychology of Money', 'author': 'Morgan Housel', 'Category': 'Finance'},
    {'title': 'Sapiens', 'author': 'Yuval Noah Harari', 'Category': 'History'},
    {'title': 'A Brief History of Time', 'author': 'Stephen Hawking', 'Category': 'Science'},
    {'title': 'The Selfish Gene', 'author': 'Richard Dawkins', 'Category': 'Science'},
    {'title': 'The Lean Startup', 'author': 'Eric Ries', 'Category': 'Business'},
    {'title': 'Think and Grow Rich', 'author': 'Napoleon Hill', 'Category': 'Self-Help'},
    {'title': 'The 7 Habits of Highly Effective People', 'author': 'Stephen R. Covey', 'Category': 'Self-Help'},
    {'title': 'The Lord of the Rings', 'author': 'J.R.R. Tolkien', 'Category': 'Fantasy'},
    {'title': 'The Silent Patient', 'author': 'Alex Michaelides', 'Category': 'Thriller'},
    {'title': 'It Ends with Us', 'author': 'Colleen Hoover', 'Category': 'Romance'},
    {'title': 'The Hunger Games', 'author': 'Suzanne Collins', 'Category': 'Science Fiction'},
    {'title': 'The Fault in Our Stars', 'author': 'John Green', 'Category': 'Romance'},
    {'title': 'The Midnight Library', 'author': 'Matt Haig', 'Category': 'Fantasy'}
]

@app.get("/books")
async def get_all_books():
    return BOOKS


@app.get("/books/{book_title}")  #for path parameter
async def get_all_books(book_title:str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book


@app.get("/books/") #for query parameter
async def get_books_by_category(category:str):
    book_to_return = []
    for book in BOOKS:
        if book.get('Category').casefold() == category.casefold():
            book_to_return.append(book)
    return book_to_return


@app.get("/books/{book_author}/") #for query parameter with path parameter
async def get_books_author_by_category(book_author:str, category:str):
    book_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and book.get('Category').casefold() == category.casefold():
            book_to_return.append(book)
    return book_to_return


@app.post("/books/create_new_book/") #Post method to create a new book
async def create_new_book(new_book=Body()):
    BOOKS.append(new_book)
    return 'New book created!'


@app.put("/books/update_book/") #Put method to update book
async def update_book(updated_book=Body()):
    for i in range (len(BOOKS)):
        if BOOKS[i].get('title') == updated_book.get('title'):
            BOOKS[i] = updated_book
    return 'Book Updated!'


@app.delete("/books/delete_book/") #Delete method to delete book
async def delete_book(title:str):
    for i in range (len(BOOKS)):
        if BOOKS[i].get('title').casefold() == title.casefold():
            BOOKS.pop(i)
    return 'Book Deleted'


@app.get("/books/byauthor/{author}") #Get books by author assignment
async def get_books_by_author(author:str):
    book_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            book_to_return.append(book)
    return book_to_return