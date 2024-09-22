from fastapi import APIRouter, HTTPException

from src.library.schemas import books, authors, books_authors
from src.library import crud
from src.database import async_session_dependency

books_router = APIRouter(prefix="/books", tags=["books"])

@books_router.get("/all", response_model=list[books_authors.BooksAuthors])
async def read_books(session: async_session_dependency
                     )-> list[books_authors.BooksAuthors]:
    try:
        books = await crud.get_books(session=session)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    if not books:
        raise HTTPException(status_code=404, detail="No books found")
    
    return books



@books_router.get("/{book_name}", response_model=books_authors.BooksAuthors)
async def read_book_by_name(
    book_name: str,
    session: async_session_dependency
):
    try:
        book = await crud.get_book_by_name(book_name=book_name, session=session)
    except Exception:
        raise HTTPException(status_code=500)
    
    if not book:
        raise HTTPException(status_code=404)
    return book


@books_router.get("/{book_name}/author", response_model=authors.AuthorRead)
async def read_author_by_book_name(
    book_name: str,
    session: async_session_dependency
):
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
    
