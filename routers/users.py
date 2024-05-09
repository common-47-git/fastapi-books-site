from datetime import timedelta
from fastapi import APIRouter, HTTPException, Response, Depends
from fastapi.security import OAuth2PasswordRequestForm
from src import database
from src.users import crud, schemas
from sqlalchemy.orm import Session

users_router = APIRouter(prefix="/users", tags=["users"])

@users_router.post("/register")
def register_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud.create_user(db=db, user=user)


@users_router.post("/login")
def login_for_access_token(
    response: Response,
    form_data: OAuth2PasswordRequestForm = Depends(), 
    db: Session = Depends(database.get_db),
    ):
    user = crud.authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=HTTPException(status_code=401),
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=crud.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = crud.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}



