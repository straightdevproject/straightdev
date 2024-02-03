from fastapi import APIRouter, Depends, status, HTTPException
from app.application.services.user_service import UserService
from app.application.services.organization_service import OrganizationService
from app.domain.models.user import UserRequest, UserResponseOrganization, OrganizationUsers
from typing import List

router = APIRouter(prefix="/api/users", tags=['Users'])

_user_service: UserService = Depends(UserService)
_organization_service: OrganizationService = Depends(OrganizationService)


@router.get("", status_code=status.HTTP_200_OK, response_model=List[UserResponseOrganization])
def get_users(
    user_service: UserService = _user_service,
):
    users = user_service.get_users()
    return users


@router.get("/{id}", response_model=UserResponseOrganization)
def get_user_by_id(
    id: int,
    user_service: UserService = _user_service
):
    return user_service.get_user_by_id(user_id=id)


@router.get("/organization/{organization_id}", response_model=OrganizationUsers)
def get_users_by_organization_id(
    organization_id: int,
    user_service: UserService = _user_service,
    organization_service: OrganizationService = _organization_service
):
    pass
    organization = organization_service.get_organization_by_id(organization_id)
    if not organization:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"organization with id {organization_id} was not found")
    users = user_service.get_users_by_organization_id(organization_id)
    return OrganizationUsers(organization=organization, users=users)


@router.post("", status_code=status.HTTP_201_CREATED, response_model=UserResponseOrganization)
def create_user(
    user: UserRequest,
    user_service: UserService = _user_service
):
    return user_service.create_user(user_data=user)
