from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel

from app.domain.models.organization import OrganizationResponse


class UserRequest(BaseModel):
    name: str
    surname: Optional[str] = None
    organization_id: int
    pass


class UserResponse(BaseModel):
    id: int
    name: str
    surname: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True


class UserResponseOrganization(BaseModel):
    id: int
    name: str
    surname: Optional[str] = None
    created_at: datetime
    organization: OrganizationResponse

    class Config:
        from_attributes = True


class OrganizationUsers(BaseModel):
    organization: OrganizationResponse
    users: List[UserResponse]
