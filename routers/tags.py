from fastapi import APIRouter, HTTPException

from src.library import crud, schemas
from src.database import async_session_dependency

tags_router = APIRouter(prefix="/tags", tags=["tags"])

@tags_router.get("/", response_model=list[schemas.TagRead])
async def read_tags(
    session: async_session_dependency
):
    try:
        tags = await crud.get_tags(session=session)
    except Exception:
        raise HTTPException(status_code=500, detail="Unexpected error occured.")
    if not tags:
        raise HTTPException(status_code=404, detail="Not a single tag was found.")
    else:
        return tags



