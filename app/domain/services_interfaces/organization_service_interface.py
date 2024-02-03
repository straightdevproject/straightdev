from abc import ABC, abstractmethod
from typing import List
from sqlalchemy.orm import Session
from app.infrastructure.schemas.organization import Organization as OrganizationSchema
from app.domain.models.organization import OrganizationRequest


class OrganizationServiceInterface(ABC):

    @abstractmethod
    def get_organizations(
        self
    ) -> List[OrganizationSchema]:
        pass

    @abstractmethod
    def get_organization_by_id(
        self,
        id: int
    ) -> OrganizationSchema:
        pass

    def get_organization_by_name(
        self,
        name: str
    ) -> OrganizationSchema:
        pass

    @abstractmethod
    def create_organization(
        self,
        organization_data: OrganizationRequest
    ) -> OrganizationSchema:
        pass
