from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm

from datetime import timedelta
from typing import Annotated

from src.users.auth import create_access_token
from src.users.crud import authenticate_user, get_current_user, get_user_books, post_user, post_a_book_to_the_current_users_library
from src.users.schemas import Token, UserRead, UserCreate
from src.library.schemas import books
from src.library import crud
from src.database import async_session_dependency
from env.config import ACCESS_TOKEN_EXPIRE_MINUTES

users_router = APIRouter(prefix="/users", tags=["users"])

@users_router.post("/login")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    session: async_session_dependency
) -> Token:
    try:
        user = await authenticate_user(session=session, username=form_data.username, password=form_data.password)
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.username}, expires_delta=access_token_expires
        )
    except Exception:
        raise HTTPException(status_code=500, detail="Unexpected error occured.")
    if not user:
        raise HTTPException(
            status_code=HTTPException(status_code=401),
            detail="Incorrect username",
            headers={"WWW-Authenticate": "Bearer"},
        )
    else:
        return Token(access_token=access_token, token_type="bearer")


@users_router.post("/new", response_model=UserRead)
async def create_user(
    session: async_session_dependency,
    user: UserCreate
) -> UserRead:
    return post_user(session=session, user=user)


@users_router.get("/me", response_model=UserRead)
async def read_current_user(
    current_user: Annotated[UserRead , Depends(get_current_user)],
) -> UserRead:
    return current_user


@users_router.get("/books", response_model=list[books.BookRead])
async def read_user_books(
    current_user: Annotated[UserRead, Depends(get_current_user)],
    session: async_session_dependency
) -> list[books.BookRead]:
    return await get_user_books(username=current_user.username, session=session)


@users_router.post("/bookmark")
async def add_a_book_to_the_current_users_library(
    book_name: str,
    shelf: str,
    current_user: Annotated[UserRead, Depends(get_current_user)],
    session: async_session_dependency
):
    try:
        book = await post_a_book_to_the_current_users_library(
            book_name=book_name, 
            username=current_user.username,
            shelf_to_put=shelf,
            session=session
        )
    except HTTPException as http_exc:
        raise http_exc
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))
    return {"status": 200, "detail": "Book added to library", "data": book}
