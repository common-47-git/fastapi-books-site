from typing import Annotated

from fastapi import Depends, HTTPException
from sqlalchemy import select, insert
from jose import JWTError, jwt # type: ignore

from env.config import ALGORITHM, SECRET_KEY
from src.database import async_session_dependency
from src.users.schemas import UserBooksCreate, UserCreate, UserInDB, TokenData, UserRead
from src.users.models import UserModel, UsersBooksModel
from src.library.models.book import BookModel
from src.users.auth import get_password_hash, oauth2_scheme, verify_password


async def get_user(
    session: async_session_dependency, 
    username: str
):
    stmt = select(UserModel).filter(UserModel.username == username)
    result = await session.execute(stmt)
    user = result.scalars().first()
    return UserInDB.model_validate(user, from_attributes=True)


def post_user(
    session: async_session_dependency,
    user: UserCreate
) -> UserRead:
    user.password = get_password_hash(user.password)
    new_user = UserModel(**user.model_dump())
    session.add(new_user)
    session.commit()
    return new_user


async def authenticate_user(
    session: async_session_dependency, 
    username: str, password: str
):
    user = await get_user(session=session, username=username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)], 
    session: async_session_dependency
):
    credentials_exception = HTTPException(
        status_code=HTTPException(status_code=401),
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
        
        user = await get_user(session=session, username=token_data.username)
        if user is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    except Exception:
        raise HTTPException(status_code=500, detail="Unexpected error occured.")
    else:
        return user


async def get_user_books(
    session: async_session_dependency, 
    username: str
):
    try:
        query = (
            select(BookModel)
            .join(UsersBooksModel)
            .join(UserModel)
            .filter(UserModel.username == username)
        )
        result = await session.execute(query)
        books = result.scalars().all()
    except Exception:
        raise HTTPException(status_code=500, detail="Unexpected error occured.")
    else:
        return books
    
    
async def post_a_book_to_the_current_users_library(
    session: async_session_dependency, 
    book_name: str,
    username: str,
    shelf_to_put: str
):
    # Fetch the book ID
    stmt = select(BookModel.book_id).where(BookModel.book_name == book_name)
    result = await session.execute(stmt)
    book_id = result.scalars().first()

    if not book_id:
        raise HTTPException(status_code=404, detail=f"Book '{book_name}' not found")

    # Fetch the user ID
    stmt = select(UserModel.user_id).where(UserModel.username == username)
    result = await session.execute(stmt)
    user_id = result.scalars().first()

    if not user_id:
        raise HTTPException(status_code=404, detail=f"User '{username}' not found")

    # Insert into the users_books table
    stmt = insert(UsersBooksModel).values(
        user_id=user_id,
        book_id=book_id,
        book_shelf=shelf_to_put
    )
    await session.execute(stmt)
    await session.commit()

    return {"user_id": user_id, "book_id": book_id, "book_shelf": shelf_to_put}


