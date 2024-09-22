from sqlalchemy import Integer, String, ForeignKey, TEXT
from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base

class ChapterModel(Base):
    __tablename__ = "chapters"
    
    chapter_id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    volume_id: Mapped[int] = mapped_column(Integer, ForeignKey("volumes.volume_id"), nullable=False)
    chapter_number: Mapped[int] = mapped_column(Integer, nullable=False)
    chapter_name: Mapped[str] = mapped_column(String(50), nullable=False)
    chapter_content: Mapped[str] = mapped_column(TEXT, nullable=False)
    
    
