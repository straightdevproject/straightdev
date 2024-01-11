from datetime import datetime
from pydantic import BaseModel

class UserBase(BaseModel):
    name: str


class UserRequest(UserBase):
    pass

class UserResponse(BaseModel):
    id: int
    name: str
    created_at: datetime

    class Config:
        from_attributes = True
