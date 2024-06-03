from fastapi import Depends

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Session

from typing import Annotated

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
        columns_values = ""
        columns_to_show = 2
        for i, column in enumerate(self.__table__.c):
            if i < columns_to_show:
                columns_values += f"{column.key}={getattr(self, column.key)} "
            else:
                continue
        return f"{self.__tablename__}({columns_values.strip()})"

