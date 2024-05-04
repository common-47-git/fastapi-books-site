from sqlalchemy import select
from sqlalchemy.orm import Session
from src.models import BooksModel, VolumeModel, ChapterModel, TagsModel

######### Books CRUD #########

async def get_books(session: Session):
    stmt = select(BooksModel)
    result = session.execute(stmt)
    books = result.scalars().all()
    
    for book in books:
        if book.book_description is None:
            book.book_description = "No description"
            
    return books


async def get_book(book_name: str, session: Session):
    stmt = select(BooksModel).where(BooksModel.book_name == book_name)
    result = session.execute(stmt)
    book = result.scalars().first()
    
    if book.book_description is None:
            book.book_description = "No description"

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
    .join(BooksModel, BooksModel.book_id == VolumeModel.book_id)
    .filter(ChapterModel.chapter_number == chapter_number)
    .filter(VolumeModel.volume_number == volume_number)
    .filter(BooksModel.book_name == book_name)
    )
    result = session.execute(query)
    chapter_content = result.scalars().first()
    return chapter_content

######### Tags CRUD #########

async def get_tags(session: Session):
    stmt = select(TagsModel)
    result = session.execute(stmt)
    books = result.scalars().all()
    return books