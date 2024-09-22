from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base

class TagModel(Base):
    __tablename__ = "tags"
    
    tag_id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    tag_name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)


