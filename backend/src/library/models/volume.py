from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base

class VolumeModel(Base):
    __tablename__ = "volumes"
    
    volume_id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    book_id: Mapped[int] = mapped_column(Integer, ForeignKey("books.book_id"), nullable=False)
    volume_number: Mapped[int] = mapped_column(Integer, nullable=False)
    volume_name: Mapped[str] = mapped_column(String(50), nullable=False)
   
    
