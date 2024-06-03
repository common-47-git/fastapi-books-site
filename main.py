from fastapi import FastAPI
from routers import books, tags, authors, users

app = FastAPI(title="Books site")

app.include_router(books.books_router)
app.include_router(authors.authors_router)
app.include_router(tags.tags_router)
app.include_router(users.users_router)