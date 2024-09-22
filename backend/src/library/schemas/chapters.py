from pydantic import BaseModel, Field

    
########### Chapters Schemas ###########

class ChapterBase(BaseModel):
    chapter_number: int
    chapter_name: str = Field(max_length=50)
    chapter_content: str


class ChapterCreate(ChapterBase):
    pass


class ChapterRead(ChapterBase):
    pass


class ChapterUpdate(ChapterBase):
    pass


class ChapterInDB(ChapterBase):
    chapter_id: int
    volume_id: int
 