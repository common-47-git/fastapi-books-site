from sqlalchemy import select
from sqlalchemy.orm import Session

from src.library.models import (
    BookModel,
    BooksAuthorsModel,
    VolumeModel,
    ChapterModel,
    TagModel, 
    AuthorModel 
)

######### Books CRUD #########

async def get_books(session: Session):
    stmt = select(BookModel)
    result = session.execute(stmt)
    books = result.scalars().all()
    
    for book in books:
        if book.book_description is None:
            book.book_description = "No description"
            
    return books


async def get_book_by_name(book_name: str, session: Session):
    stmt = select(BookModel).where(BookModel.book_name == book_name)
    result = session.execute(stmt)
    book = result.scalars().first()
    return book


async def get_book_chapter(
    book_name: str, 
    volume_number: int, 
    chapter_number: int, 
    session: Session
    ):

    query = (
    select(ChapterModel.chapter_content)
    .join(VolumeModel, VolumeModel.volume_id == ChapterModel.volume_id)
    .join(BookModel, BookModel.book_id == VolumeModel.book_id)
    .filter(ChapterModel.chapter_number == chapter_number)
    .filter(VolumeModel.volume_number == volume_number)
    .filter(BookModel.book_name == book_name)
    )
    result = session.execute(query)
    chapter_content = result.scalars().first()
    return chapter_content

######### Tags CRUD #########

async def get_tags(session: Session):
    stmt = select(TagModel)
    result = session.execute(stmt)
    books = result.scalars().all()
    return books

######### Authors CRUD #########

async def get_authors(session: Session):
    stmt = select(AuthorModel)
    result = session.execute(stmt)
    authors = result.scalars().all()
    print(authors)
      
    return authors

async def get_books_by_author(author_name: str, session: Session):
    stmt = (
        select(BookModel)
        .join(BooksAuthorsModel)
        .join(AuthorModel)
        .where(AuthorModel.author_name == author_name))
    result = session.execute(stmt)
    books = result.scalars().all()
    return books