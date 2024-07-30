from fastapi import APIRouter, HTTPException

from src.library import schemas
from src.library import crud
from src.database import async_session_dependency

authors_router = APIRouter(prefix="/authors", tags=["authors"])

@authors_router.get("/", response_model=list[schemas.AuthorRead])
async def read_authors(
    session: async_session_dependency
):
    try:
        authors = await crud.get_authors(session=session)  
    except Exception:
        raise HTTPException(status_code=500)
    
    if not authors:
        raise HTTPException(status_code=404)
    return authors


@authors_router.get("/{author_name}", response_model=list[schemas.BookRead])
async def read_books_by_author(
    author_name: str,
    session: async_session_dependency
):
    try:
        books = await crud.get_books_by_author(author_name=author_name, session=session)
    except Exception:
        raise HTTPException(status_code=500)
    
    if not books:
        raise HTTPException(status_code=404)
    return books


