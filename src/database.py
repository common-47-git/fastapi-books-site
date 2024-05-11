from fastapi import Depends

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Session

from typing import Annotated

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

engine = create_engine(
    "mssql+pyodbc://books-site-login:121212@AYANOKOUJI-PC\SQLSERVER/books-site?driver=SQL+Server",
    echo=True)

session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()
        
db_dependency = Annotated[Session, Depends(get_db)]

class Base(DeclarativeBase):
    def __repr__(self) -> str:
        return f"<OBJ({self.__table__.c[0].key}={getattr(self, self.__table__.c[0].key)} {self.__table__.c[1].key}={getattr(self, self.__table__.c[1].key)})>"
