from sqlalchemy import Column, ForeignKey, Table
from src.database import Base
    
#class BooksAuthorsModel(Base):
#    __tablename__ = "books-authors"
#    
#    book_id: Mapped[int] = mapped_column(Integer, ForeignKey("books.book_id"), primary_key=True, nullable=False)
#    author_id: Mapped[int] = mapped_column(Integer, ForeignKey("authors.author_id"), primary_key=True, nullable=False)    


BooksAuthorsModel = Table(
    "books_authors",
    Base.metadata,
    Column("book_id", ForeignKey("books.book_id"), primary_key=True, nullable=False),
    Column("author_id", ForeignKey("authors.author_id"), primary_key=True, nullable=False),
)