from sqlalchemy import Column, ForeignKey, Table, Integer, String, DATE
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


class BookModel(Base):
    __tablename__ = "books"
    
    book_id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    book_name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    book_country: Mapped[str] = mapped_column(String(50), nullable=True)
    book_release_date: Mapped[DATE] = mapped_column(DATE, nullable=True)
    book_translation_status: Mapped[str] = mapped_column(String(50), nullable=True)
    book_description: Mapped[str] = mapped_column(String(1500), nullable=True)
    book_cover: Mapped[str] = mapped_column(String(500), nullable=False)
    
    book_authors: Mapped[list["AuthorModel"]] = relationship(
        back_populates="author_books",
        secondary=BooksAuthorsModel,
    )


class AuthorModel(Base):
    __tablename__ = "authors"
    
    author_id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    author_name: Mapped[str] = mapped_column(String(50), nullable=True)
    author_surname: Mapped[str] = mapped_column(String(50), nullable=True)
    
    author_books: Mapped[list["BookModel"]] = relationship(
        back_populates="book_authors",
        secondary=BooksAuthorsModel,
    )
