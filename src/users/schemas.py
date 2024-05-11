from pydantic import BaseModel

########### Tokens Schemas ###########

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None

########### Users Schemas ###########

class UserBase(BaseModel):
    username: str
    email: str
    disabled: bool | None = None
    

class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class UserInDB(UserBase):
    password: str
    user_id: int
    
########### Users-Books Schemas ###########

class UserBooksBase(BaseModel):
    user_id: int
    book_id: int