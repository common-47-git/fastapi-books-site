from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm

from datetime import timedelta
from typing import Annotated
from dotenv import load_dotenv
from os import getenv

from src import database
from src.users.auth import create_access_token
from src.users.crud import authenticate_user, get_current_active_user, get_user_books 
from src.users.schemas import Token, UserRead
from src.library.schemas import BookRead

users_router = APIRouter(prefix="/users", tags=["users"])

load_dotenv(".env\.env")

@users_router.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    session: database.db_dependency
) -> Token:
    user = authenticate_user(session=session, username=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(
            status_code=HTTPException(status_code=401),
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=int(getenv("ACCESS_TOKEN_EXPIRE_MINUTES")))
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")


@users_router.get("/me", response_model=UserRead)
async def read_current_user(
    current_user: Annotated[UserRead , Depends(get_current_active_user)],
) -> UserRead:
    return current_user


@users_router.get("/me/books", response_model=list[BookRead])
async def read_user_books(
    current_user: Annotated[UserRead, Depends(get_current_active_user)],
    session: database.db_dependency
) -> list[BookRead]:
    return await get_user_books(username=current_user.username, session=session)
