from fastapi import APIRouter
from src import crud, database, schemas
from sqlalchemy.orm import Session
from fastapi import Depends

books_router = APIRouter(prefix="/books", tags=["books"])

@books_router.get("/", response_model=list[schemas.BookGet])
async def read_books(session: Session = Depends(database.get_db)):
    return await crud.get_books(session=session)


@books_router.get("/{book_name}", response_model=schemas.BookGet)
async def read_book(book_name: str, session: Session = Depends(database.get_db)):
    return await crud.get_book(book_name=book_name, session=session)

@books_router.get("/{book_name}/{volume_number}/{chapter_number}")
async def read_book(book_name: str, volume_number: int, chapter_number: int, session: Session = Depends(database.get_db)):
    return await crud.get_book_chapter(book_name=book_name, volume_number=volume_number, chapter_number=chapter_number, session=session)

