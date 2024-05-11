from typing import Annotated
from dotenv import load_dotenv
from os import getenv

from fastapi import Depends, HTTPException
from sqlalchemy import select
from jose import JWTError, jwt # type: ignore

from src import database
from src.users.schemas import UserInDB, TokenData, UserRead
from src.users.models import UserModel, UsersBooksModel
from src.library.models import BookModel
from src.users.auth import oauth2_scheme, verify_password

load_dotenv(".env\.env")

def get_user(
    session: database.db_dependency, 
    username: str
):
    stmt = select(UserModel).filter(UserModel.username == username)
    result = session.execute(stmt)
    user = result.scalars().first()
    return UserInDB.model_validate(user, from_attributes=True)


def authenticate_user(
    session: database.db_dependency, 
    username: str, password: str
):
    user = get_user(session=session, username=username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)], 
    session: database.db_dependency
):
    credentials_exception = HTTPException(
        status_code=HTTPException(status_code=401),
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, getenv("SECRET_KEY"), algorithms=[getenv("ALGORITHM")])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(session=session, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(
    current_user: Annotated[UserRead, Depends(get_current_user)],
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


async def get_user_books(
    session: database.db_dependency, 
    username: str
):
    query = (
        select(BookModel)
        .join(UsersBooksModel)
        .join(UserModel)
        .filter(UserModel.username == username)
    )
    books = session.execute(query).scalars().all()
    return books
