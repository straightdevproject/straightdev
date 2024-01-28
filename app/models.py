from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel

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


class UserBase(BaseModel):
    name: str
    surname: Optional[str] = None


class UserRequest(UserBase):
    organization_id: int
    pass


class UserResponseWithOrganization(UserBase):
    id: int
    organization: OrganizationResponse
    created_at: datetime

    class Config:
        from_attributes = True


class UserResponseWithoutOrganization(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class OrganizationUsers(BaseModel):
    organization: OrganizationResponse
    users: List[UserResponseWithoutOrganization]
