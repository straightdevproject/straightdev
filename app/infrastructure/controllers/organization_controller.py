from fastapi import APIRouter, Depends, status, HTTPException
from app.application.services.organization_service import OrganizationService
from app.domain.models.organization import OrganizationRequest, OrganizationResponse
from typing import List

router = APIRouter(prefix="/api/organizations", tags=['Organizations'])

_organization_service: OrganizationService = Depends(OrganizationService)


@router.get("", status_code=status.HTTP_200_OK, response_model=List[OrganizationResponse])
def get_organizations(
        organization_service: OrganizationService = _organization_service,
):
    return organization_service.get_organizations()


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=OrganizationResponse)
def get_organization_by_id(
        id: int,
        organization_service: OrganizationService = _organization_service,
):
    organization = organization_service.get_organization_by_id(id)
    if not organization:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"organization with id {id} was not found")
    return organization


@router.post("", status_code=status.HTTP_201_CREATED, response_model=OrganizationResponse)
def create_organization(
    organization_data: OrganizationRequest,
    organization_service: OrganizationService = _organization_service
):
    organization = organization_service.get_organization_by_name(organization_data.name)
    if organization:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"organization with name {organization.name} already exists")
    return organization_service.create_organization(organization_data=organization_data)
