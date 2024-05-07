from fastapi import APIRouter, Body
from src import database
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from typing import Annotated

from src.library import crud, schemas

books_router = APIRouter(prefix="/books", tags=["books"])

@books_router.get("/", response_model=list[schemas.BookRead])
async def read_books(session: Session = Depends(database.get_db)):
    books = await crud.get_books(session=session)
    if not books:
        raise HTTPException(status_code=404)
    return books


@books_router.get("/{book_name}", response_model=schemas.BookRead)
async def read_book(book_name: str, session: Session = Depends(database.get_db)) -> schemas.BookRead:
    book = await crud.get_book_by_name(book_name=book_name, session=session)
    if not book:
        raise HTTPException(status_code=404)
    return book


@books_router.get("/{book_name}/{volume_number}/{chapter_number}")
async def read_book_chapter(
    book_name: str, 
    volume_number: int, 
    chapter_number: int, 
    session: Session = Depends(database.get_db)
    ):
    chapter = await crud.get_book_chapter(book_name=book_name, 
                                          volume_number=volume_number, 
                                          chapter_number=chapter_number, 
                                          session=session)
    if not chapter:
        raise HTTPException(status_code=404)
    return chapter


@books_router.get("/{book_name}", response_model=schemas.BookRead)
async def read_book(
    book_name: str, 
    session: Session = Depends(database.get_db)
    ) -> schemas.BookRead:
    book = await crud.get_book_by_name(book_name=book_name, session=session)
    if not book:
        raise HTTPException(status_code=404)
    return book