from pydantic import BaseModel, Field
from datetime import date

########### Books Schemas ###########

class BookBase(BaseModel):
    book_name: str = Field(max_length=50)
    book_country: str | None = Field(default=None, max_length=50)
    book_release_date: date | None = None
    book_translation_status: str | None = Field(default=None, max_length=50)
    book_description: str | None = Field(default=None, max_length=1500)
    

class BookCreate(BookBase):
    pass


class BookRead(BookBase):
    pass


class BookUpate(BookBase):
    pass


class BookInDB(BookBase):
    book_id: int

########### Tags Schemas ###########

class TagBase(BaseModel):
    tag_name: str = Field(max_length=50)
    

class TagCreate(TagBase):
    pass


class TagRead(TagBase):
    pass


class TagUpdate(TagBase):
    pass


class TagInDB(TagBase):
    tag_id: int
    

########### Volumes Schemas ###########

class VolumeBase(BaseModel):
    book_id: int
    volume_number: int
    volume_name: str = Field(max_length=50)
    

class VolumeCreate(VolumeBase):
    pass


class VolumeUpdate(VolumeBase):
    pass


class VolumeRead(VolumeBase):
    pass


class VolumeInDB(VolumeBase):
    volume_id: int
    
########### Chapters Schemas ###########

class ChapterBase(BaseModel):
    chapter_number: int
    chapter_name: str = Field(max_length=50)
    chapter_content: str


class ChapterCreate(VolumeBase):
    pass


class ChapterRead(VolumeBase):
    pass


class ChapterUpdate(VolumeBase):
    pass


class ChapterInDB(VolumeBase):
    chapter_id: int
    volume_id: int
    
########### Authors Schemas ###########

class AuthorBase(BaseModel):
    author_name: str = Field(max_length=50)
    author_surname: str = Field(max_length=50)


class AuthorCreate(AuthorBase):
    pass


class AuthorRead(AuthorBase):
    pass


class AuthorInDB(AuthorBase):
    author_id: int