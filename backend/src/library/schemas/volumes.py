from pydantic import BaseModel, Field
from datetime import date

########### Volumes Schemas ###########

class VolumeBase(BaseModel):
    book_id: int
    volume_number: int
    volume_name: str = Field(max_length=50)
    

class VolumeCreate(VolumeBase):
    pass


class VolumeUpdate(VolumeBase):
    pass


class VolumeRead(VolumeBase):
    pass


class VolumeInDB(VolumeBase):
    volume_id: int
    