from fastapi import FastAPI
from routers import books, tags

app = FastAPI()

app.include_router(books.books_router)
app.include_router(tags.tags_router)