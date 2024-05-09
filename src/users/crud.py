from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt # type: ignore
from sqlalchemy import select
from sqlalchemy.orm import Session
from src.users import schemas, models
from passlib.context import CryptContext # type: ignore

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user_by_username(session: Session, username: str):
    stmt = select(models.UserModel).filter(models.UserModel.username == username)
    result = session.execute(stmt)
    user = result.scalars().first()
    return user


def create_user(db: Session, user: schemas.UserCreate):
    password = pwd_context.hash(user.password)
    db_user = models.UserModel(username=user.username, password=password, email=user.email)
    db.add(db_user)
    db.commit()
    return "complete"



def authenticate_user(username: str, password: str, db: Session):
    stmt = select(models.UserModel).filter(models.UserModel.username == username)
    result = db.execute(stmt)
    user = result.scalars().first()
    if not user:
        return False
    if not pwd_context.verify(password, user.password):
        return False
    return user


def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=403, detail="Token is invalid or expired")
        return payload
    except JWTError:
        raise HTTPException(status_code=403, detail="Token is invalid or expired")


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
