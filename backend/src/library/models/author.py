from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.library.models.book import BookModel
from src.library.models.books_authors import BooksAuthorsModel
from src.database import Base
    
class AuthorModel(Base):
    __tablename__ = "authors"
    
    author_id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    author_name: Mapped[str] = mapped_column(String(50), nullable=True)
    author_surname: Mapped[str] = mapped_column(String(50), nullable=True)
    
    author_books: Mapped[list["BookModel"]] = relationship(
        back_populates="book_authors",
        secondary=BooksAuthorsModel,
    )


