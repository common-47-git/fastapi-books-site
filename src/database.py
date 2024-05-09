from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
import redis

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


class Base(DeclarativeBase):
    def __repr__(self) -> str:
        return f"<OBJ({self.__table__.c[0].key}={getattr(self, self.__table__.c[0].key)} {self.__table__.c[1].key}={getattr(self, self.__table__.c[1].key)})>"
