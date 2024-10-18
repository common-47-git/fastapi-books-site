from sqlalchemy import Integer, String, DATE
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.library.models.books_authors import BooksAuthorsModel
from src.database import Base
    

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
        secondary="books_authors",
    )