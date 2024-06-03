from datetime import date

from sqlalchemy import Integer, String, ForeignKey, DATE
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class UserModel(Base):
    __tablename__ = "users"
    
    user_id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(50), nullable=False)
    registration_date: Mapped[date] = mapped_column(DATE, default=date.today(), nullable=True)


class UsersBooksModel(Base):
    __tablename__ = "users-books"
    
    book_id: Mapped[int] = mapped_column(Integer, ForeignKey("books.book_id"), primary_key=True, nullable=False)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.user_id"), primary_key=True, nullable=False)

