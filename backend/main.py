from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers import books, tags, authors, users


app = FastAPI(title="Books site")

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                   "Authorization"],
)

app.include_router(books.books_router)
app.include_router(authors.authors_router)
app.include_router(tags.tags_router)
app.include_router(users.users_router)
