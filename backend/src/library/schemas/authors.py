from pydantic import BaseModel, Field

class AuthorBase(BaseModel):
    author_name: str = Field(max_length=50)
    author_surname: str = Field(max_length=50)


class AuthorCreate(AuthorBase):
    pass

class AuthorRead(AuthorBase):
    pass

class AuthorInDB(AuthorBase):
    author_id: int
    