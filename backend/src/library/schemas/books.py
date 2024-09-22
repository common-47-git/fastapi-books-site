from pydantic import BaseModel, Field
from datetime import date

class BookBase(BaseModel):
    book_name: str = Field(max_length=50)
    book_country: str | None = Field(default=None, max_length=50)
    book_release_date: date | None = None
    book_translation_status: str | None = Field(default=None, max_length=50)
    book_description: str | None = Field(default=None, max_length=1500)
    book_cover: str = Field(default="https://ranobehub.org/img/ranobe/posters/default.jpg", max_length=500)


class BookCreate(BookBase):
    pass
  
class BookRead(BookBase):
    pass

class BookUpate(BookBase):
    pass

class BookInDB(BookBase):
    book_id: int