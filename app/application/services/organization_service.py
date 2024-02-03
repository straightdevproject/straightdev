from app.domain.services_interfaces.organization_service_interface import OrganizationServiceInterface
from app.infrastructure.repositories.organization_repository import OrganizationRepository
from fastapi import Depends
from app.domain.models.organization import OrganizationRequest
from app.infrastructure.schemas.organization import Organization as OrganizationSchema
from typing import List


class OrganizationService(OrganizationServiceInterface):
    def __init__(
        self,
        organization_repository: OrganizationRepository = Depends(OrganizationRepository),
    ):
        self._organization_repository = organization_repository

    def get_organizations(
        self
    ) -> List[OrganizationSchema]:
        return self._organization_repository.get_organizations()

    def get_organization_by_id(
        self,
        id: int
    ) -> OrganizationSchema:
        return self._organization_repository.get_organization_by_id(id)

    def get_organization_by_name(
        self,
        name: str
    ) -> OrganizationSchema:
        return self._organization_repository.get_organization_by_name(name)

    def create_organization(
        self,
        organization_data: OrganizationRequest
    ) -> OrganizationSchema:
        return self._organization_repository.create_organization(organization_data)
