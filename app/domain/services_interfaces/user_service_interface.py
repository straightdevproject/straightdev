from abc import ABC, abstractmethod
from typing import List
from sqlalchemy.orm import Session
from app.infrastructure.schemas.user import User as UserSchema
from app.domain.models.user import UserRequest


class UserServiceInterface(ABC):

    @abstractmethod
    def get_users(
        self
    ) -> List[UserSchema]:
        pass

    @abstractmethod
    def get_user_by_id(
        self,
        user_id: int
    ) -> UserSchema:
        pass

    @abstractmethod
    def get_users_by_organization_id(
        self,
        organization_id: int
    ) -> List[UserSchema]:
        pass

    @abstractmethod
    def create_user(
        self,
        user_data: UserRequest
    ) -> UserSchema:
        pass
