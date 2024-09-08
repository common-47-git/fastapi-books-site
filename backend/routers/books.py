from fastapi import APIRouter, HTTPException

from src.library import schemas
from src.library import crud
from src.database import async_session_dependency

books_router = APIRouter(prefix="/books", tags=["books"])

@books_router.get("/", response_model=list[schemas.BookRead])
async def read_books(
    session: async_session_dependency
) -> list[schemas.BookRead]:
    try:
        books = await crud.get_books(session=session)
    except Exception:
        raise HTTPException(status_code=500)
    
    if not books:
            raise HTTPException(status_code=404)
    return books


@books_router.get("/{book_name}", response_model=schemas.BookRead)
async def read_book_by_name(
    book_name: str,
    session: async_session_dependency
) -> schemas.BookRead:
    try:
        book = await crud.get_book_by_name(book_name=book_name, session=session)
    except Exception:
        raise HTTPException(status_code=500)
    
    if not book:
        raise HTTPException(status_code=404)
    return book


@books_router.get("/{book_name}/author", response_model=schemas.AuthorRead)
async def read_author_by_book_name(
    book_name: str,
    session: async_session_dependency
) -> schemas.BookRead:
    try:
        book = await crud.get_book_author_by_name(book_name=book_name, session=session)
    except Exception:
        raise HTTPException(status_code=500)
    
    if not book:
        raise HTTPException(status_code=404)
    return book


@books_router.get("/{book_name}/read")
async def read_book_chapter(
    session: async_session_dependency,
    book_name: str, 
    volume: int = 1,
    chapter: int = 1,
):
    try:
        chapter = await crud.get_book_chapter(
            book_name=book_name, 
            volume_number=volume, 
            chapter_number=chapter,
            session=session
        )
    except Exception:
        raise HTTPException(status_code=500)
    
    if not chapter:
        raise HTTPException(status_code=404)
    return chapter
    
