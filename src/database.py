from fastapi import Depends
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase

from typing import Annotated

from env.config import DBNAME, DRIVER, PASSWORD, SERVERNAME, LOGIN_USER

engine = create_async_engine(
    f"mssql+aioodbc://{LOGIN_USER}:{PASSWORD}@{SERVERNAME}/{DBNAME}?driver={DRIVER}",
    echo=True
)

session_local = async_sessionmaker(autocommit=False, autoflush=False, bind=engine)

async def get_session():
    session = session_local()
    try:
        yield session
    finally:
        session.close()
        
async_session_dependency = Annotated[AsyncSession, Depends(get_session)]

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

