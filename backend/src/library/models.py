from sqlalchemy import Integer, String, DATE, ForeignKey, TEXT
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date
from src.database import Base

class BookModel(Base):
    __tablename__ = "books"
    
    book_id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    book_name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    book_country: Mapped[str] = mapped_column(String(50), nullable=True)
    book_release_date: Mapped[date] = mapped_column(DATE, nullable=True)
    book_translation_status: Mapped[str] = mapped_column(String(50), nullable=True)
    book_description: Mapped[str] = mapped_column(String(1500), nullable=True)


class TagModel(Base):
    __tablename__ = "tags"
    
    tag_id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    tag_name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)

 
class BooksTagsModel(Base):
    __tablename__ = "books-tags"
    
    book_id: Mapped[int] = mapped_column(Integer, ForeignKey("books.book_id"), primary_key=True, nullable=False)
    tag_id: Mapped[int] = mapped_column(Integer, ForeignKey("tags.tag_id"), primary_key=True, nullable=False)
    

class VolumeModel(Base):
    __tablename__ = "volumes"
    
    volume_id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    book_id: Mapped[int] = mapped_column(Integer, ForeignKey("books.book_id"), nullable=False)
    volume_number: Mapped[int] = mapped_column(Integer, nullable=False)
    volume_name: Mapped[str] = mapped_column(String(50), nullable=False)
   
    
class ChapterModel(Base):
    __tablename__ = "chapters"
    
    chapter_id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    volume_id: Mapped[int] = mapped_column(Integer, ForeignKey("volumes.volume_id"), nullable=False)
    chapter_number: Mapped[int] = mapped_column(Integer, nullable=False)
    chapter_name: Mapped[str] = mapped_column(String(50), nullable=False)
    chapter_content: Mapped[str] = mapped_column(TEXT, nullable=False)
    
    
class AuthorModel(Base):
    __tablename__ = "authors"
    
    author_id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    author_name: Mapped[str] = mapped_column(String(50), nullable=True)
    author_surname: Mapped[str] = mapped_column(String(50), nullable=True)
    
    
class BooksAuthorsModel(Base):
    __tablename__ = "books-authors"
    
    book_id: Mapped[int] = mapped_column(Integer, ForeignKey("books.book_id"), primary_key=True, nullable=False)
    author_id: Mapped[int] = mapped_column(Integer, ForeignKey("authors.author_id"), primary_key=True, nullable=False)    
