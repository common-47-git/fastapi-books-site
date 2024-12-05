from pydantic import BaseModel

from src.library.schemas import books, tags, authors

class BookInfoBase(BaseModel):
    book: books.BookRead
    book_tags: list[tags.TagRead]
    book_authors: list[authors.AuthorRead]
    book_shelf: str | None


class BookInfoCreate(BookInfoBase):
    pass
  

class BookInfoRead(BookInfoBase):
    pass


class BookInfoUpate(BookInfoBase):
    pass
