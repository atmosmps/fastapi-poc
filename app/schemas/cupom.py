from typing import Optional

from pydantic import BaseModel


# Shared properties
class CupomBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


# Properties to receive on item creation
class CupomCreate(CupomBase):
    title: str
    description: str


# Properties to receive on item update
class CupomUpdate(CupomBase):
    pass


# Properties shared by models stored in DB
class CupomInDBBase(CupomBase):
    id: int
    title: str
    # owner_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Cupom(CupomInDBBase):
    pass


# Properties properties stored in DB
class CupomInDB(CupomInDBBase):
    pass
