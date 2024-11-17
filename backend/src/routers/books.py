from fastapi import APIRouter, HTTPException

from src.library.schemas import books, authors, book_info
from src.library import crud
from src.database import async_session_dependency

books_router = APIRouter(prefix="/books", tags=["books"])

@books_router.get("/all", response_model=list[books.BookBase])
async def read_books(session: async_session_dependency
                     )-> list[books.BookBase]:
    try:
        books = await crud.get_books(session=session)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    if not books:
        raise HTTPException(status_code=404, detail="No books found")
    
    return books


@books_router.get("/{book_name}", response_model=book_info.BookInfoRead)
async def read_book_by_name(
    book_name: str,
    session: async_session_dependency
):
    try:
        book = await crud.get_book_by_name(book_name=book_name, session=session)
        book_tags = await crud.get_tags_by_book_name(book_name=book_name, session=session)
        book_authors = await crud.get_authors_by_book_name(book_name=book_name, session=session)
    except Exception:
        raise HTTPException(status_code=500)
    
    if not book:
        raise HTTPException(status_code=404)
    return {"book": book, "book_tags": book_tags, "book_authors": book_authors}


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
    
