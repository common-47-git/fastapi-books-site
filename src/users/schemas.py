from datetime import date

from pydantic import BaseModel, EmailStr

########### Tokens Schemas ###########

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None

########### Users Schemas ###########

class UserBase(BaseModel):
    username: str
    email: EmailStr
    

class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    registration_date: date | None = None
    disabled: bool | None = None


class UserUpdate(UserBase):
    pass


class UserInDB(UserBase):
    disabled: bool | None = None
    registration_date: date
    password: str
    user_id: int
    
########### Users-Books Schemas ###########

class UserBooksBase(BaseModel):
    user_id: int
    book_id: int