from sqlalchemy import Column, ForeignKey, Table
from src.database import Base
    
BooksTagsModel = Table(
    "books_tags",
    Base.metadata,
    Column("book_id", ForeignKey("books.book_id"), primary_key=True, nullable=False),
    Column("tag_id", ForeignKey("tags.tag_id"), primary_key=True, nullable=False),
)