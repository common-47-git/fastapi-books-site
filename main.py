from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import books, tags, authors, users


app = FastAPI(title="Books site")

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(books.books_router)
app.include_router(authors.authors_router)
app.include_router(tags.tags_router)
app.include_router(users.users_router)