from sqlalchemy import Column, Integer, String, DATE, ForeignKey, TEXT, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.database import Base

    
#class BooksAuthorsModel(Base):
#    __tablename__ = "books-authors"
#    
#    book_id: Mapped[int] = mapped_column(Integer, ForeignKey("books.book_id"), primary_key=True, nullable=False)
#    author_id: Mapped[int] = mapped_column(Integer, ForeignKey("authors.author_id"), primary_key=True, nullable=False)    


BooksAuthorsModel = Table(
    "books-authors",
    Base.metadata,
    Column("book_id", ForeignKey("books.book_id"), primary_key=True, nullable=False),
    Column("author_id", ForeignKey("authors.author_id"), primary_key=True, nullable=False),
)