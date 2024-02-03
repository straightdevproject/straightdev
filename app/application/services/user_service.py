from app.domain.services_interfaces.user_service_interface import UserServiceInterface
from app.infrastructure.repositories.user_repository import UserRepository
from fastapi import Depends
from app.domain.models.user import UserRequest
from app.infrastructure.schemas.user import User as UserSchema
from typing import List


class UserService(UserServiceInterface):
    def __init__(
        self,
        user_repository: UserRepository = Depends(UserRepository),
    ):
        self._user_repository = user_repository

    def get_users(
        self
    ) -> List[UserSchema]:
        return self._user_repository.get_users()

    def get_user_by_id(
        self,
        user_id: int
    ) -> UserSchema:
        return self._user_repository.get_user_by_id(user_id)

    def get_users_by_organization_id(
        self,
        organization_id: int
    ) -> List[UserSchema]:
        return self._user_repository.get_users_by_organization_id(organization_id)

    def create_user(
        self,
        user_data: UserRequest
    ) -> UserSchema:
        return self._user_repository.create_user(user_data)
