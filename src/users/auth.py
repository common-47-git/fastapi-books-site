from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
from os import getenv

from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext # type: ignore
from jose import jwt # type: ignore

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

load_dotenv(".env\.env")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def create_access_token(
    data: dict, 
    expires_delta: timedelta | None = None
):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, getenv("SECRET_KEY"), algorithm=getenv("ALGORITHM"))
    return encoded_jwt
