from pydantic import BaseModel, Field

########### Tags Schemas ###########

class TagBase(BaseModel):
    tag_name: str = Field(max_length=50)
    

class TagCreate(TagBase):
    pass


class TagRead(TagBase):
    pass


class TagUpdate(TagBase):
    pass


class TagInDB(TagBase):
    tag_id: int
    
