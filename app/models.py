from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    surname: Optional[str] = None


class UserRequest(UserBase):
    pass


class UserResponse(BaseModel):
    id: int
    name: str
    surname: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True


class OrganizationBase(BaseModel):
    name: str


class OrganizationRequest(OrganizationBase):
    pass


class OrganizationResponse(BaseModel):
    id: int
    name: str
    created_at: datetime

    class Config:
        from_attributes = True
