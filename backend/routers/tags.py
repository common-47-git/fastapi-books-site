from fastapi import APIRouter, Depends, HTTPException

from src.library import schemas
from src.library import crud
from src.database import async_session_dependency

tags_router = APIRouter(prefix="/tags", tags=["tags"])


@tags_router.get("/", response_model=list[schemas.TagRead])
async def read_tags(
    session: async_session_dependency
):
    try:
        tags = await crud.get_tags(session=session)
    except Exception:
        raise HTTPException(status_code=500)
    
    if not tags:
        raise HTTPException(status_code=404)
    return tags
