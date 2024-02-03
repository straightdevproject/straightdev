from app.infrastructure.schemas.organization import Base as OrganizationBase
from app.infrastructure.schemas.user import Base as UserBase

Base = [UserBase, OrganizationBase]