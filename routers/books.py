from fastapi import APIRouter, HTTPException

from typing import Annotated

from src.library import crud, schemas
from src.database import async_session_dependency

books_router = APIRouter(prefix="/books", tags=["books"])

@books_router.get("/", response_model=list[schemas.BookRead])
async def read_books(
    session: async_session_dependency
) -> list[schemas.BookRead]:
    try:
        books = await crud.get_books(session=session)
    except Exception:
        raise HTTPException(status_code=500, detail="Unexpected error occured.")
    if not books:
            raise HTTPException(status_code=404, detail="Not a single book was found.")
    else:
        return books


@books_router.get("/{book_name}", response_model=schemas.BookRead)
async def read_book(
    book_name: str,
    session: async_session_dependency
) -> schemas.BookRead:
    try:
        book = await crud.get_book_by_name(book_name=book_name, session=session)
    except Exception:
        raise HTTPException(status_code=500, detail="Unexpected error occured.")
    if not book:
        raise HTTPException(status_code=404, detail="Book not found.")
    else:
        return book


@books_router.get("/{book_name}/{volume}/{chapter}")
async def read_book_chapter(
    book_name: str, 
    volume: int, 
    chapter: int, 
    session: async_session_dependency
):
    try:
        chapter = await crud.get_book_chapter(
            book_name=book_name, 
            volume_number=volume, 
            chapter_number=chapter,
            session=session
        )
    except Exception:
        raise HTTPException(status_code=500, detail="Unexpected error occured.")
    if not chapter:
        raise HTTPException(status_code=404, detail="Chapter not found")
    else:
        return chapter
    
