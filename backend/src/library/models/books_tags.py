from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from backend.src.library.models.books_authors import BooksAuthorsModel
from src.database import Base

 
class BooksTagsModel(Base):
    __tablename__ = "books-tags"
    
    book_id: Mapped[int] = mapped_column(Integer, ForeignKey("books.book_id"), primary_key=True, nullable=False)
    tag_id: Mapped[int] = mapped_column(Integer, ForeignKey("tags.tag_id"), primary_key=True, nullable=False)
    


