from fastapi import APIRouter
from src import database
from sqlalchemy.orm import Session
from fastapi import Depends

from src.library import crud, schemas

tags_router = APIRouter(prefix="/tags", tags=["tags"])

@tags_router.get("/", response_model=list[schemas.TagRead])
async def read_tags(
    session: Session = Depends(database.get_db)
):
    return await crud.get_tags(session=session)



