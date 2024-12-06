from fastapi import APIRouter, HTTPException, Depends


from src.library.schemas import books, authors, book_info
from src.library import crud as library_crud
from src.users.schemas import UserRead
from src.users import crud as users_crud
from src.database import async_session_dependency

from typing import Annotated

books_router = APIRouter(prefix="/books", tags=["books"])

@books_router.get("/all", response_model=list[books.BookBase])
async def read_books(
    session: async_session_dependency
)-> list[books.BookBase]:
    try:
        books = await library_crud.get_books(session=session)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    if not books:
        raise HTTPException(status_code=404, detail="No books found")
    
    return books


@books_router.get("/{book_name}", response_model=book_info.BookInfoRead)
async def read_book_by_name(
    book_name: str,
    session: async_session_dependency,
    token: str | None = None,
):
    try:
        
        book = await library_crud.get_book_by_name(book_name=book_name, session=session)
        if not book:
            raise HTTPException(status_code=404, detail="Book not found.")
        
        book_tags = await library_crud.get_tags_by_book_name(book_name=book_name, session=session)
        book_authors = await library_crud.get_authors_by_book_name(book_name=book_name, session=session)

        if not token:
            book_shelf = None
        else:
            current_user = await users_crud.get_current_user(token=token, session=session)
            book_shelf = await users_crud.get_user_book_shelf(
                book_name=book_name,
                username=current_user.username,
                session=session
            )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected server error: {str(e)}")
    
    return {
            "book": book,
            "book_tags": book_tags,
            "book_authors": book_authors,
            "book_shelf": book_shelf}


@books_router.get("/{book_name}/read")
async def read_book_chapter(
    session: async_session_dependency,
    book_name: str, 
    volume: int = 1,
    chapter: int = 1,
):
    try:
        chapter = await library_crud.get_book_chapter(
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
    
