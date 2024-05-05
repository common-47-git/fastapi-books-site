from fastapi import APIRouter
from src import crud, database, schemas
from sqlalchemy.orm import Session
from fastapi import Depends

tags_router = APIRouter(prefix="/tags", tags=["tags"])

@tags_router.get("/", response_model=list[schemas.TagRead])
async def read_tags(session: Session = Depends(database.get_db)):
    return await crud.get_tags(session=session)

