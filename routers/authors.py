from fastapi import APIRouter
from src import crud, database, schemas
from sqlalchemy.orm import Session
from fastapi import Depends

authors_router = APIRouter(prefix="/authors", tags=["authors"])

@authors_router.get("/", response_model=list[schemas.AuthorRead])
async def read_authors(session: Session = Depends(database.get_db)):
    return await crud.get_authors(session=session)


@authors_router.get("/{author_name}", response_model=list[schemas.BookRead])
async def read_books_by_author(author_name: str, session: Session = Depends(database.get_db)):
    return await crud.get_books_by_author(author_name=author_name, session=session)


