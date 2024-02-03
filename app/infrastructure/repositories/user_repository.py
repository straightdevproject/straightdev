from sqlalchemy.orm import Session
from app.domain.repositories_interfaces.user_repository_interface import UserRepositoryInterface
from app.infrastructure.schemas.user import User as UserSchema
from fastapi import Depends
from app.infrastructure.database.database import get_db
from app.domain.models.user import UserRequest
from typing import List


class UserRepository(UserRepositoryInterface):

    def __init__(
            self,
            db: Session = Depends(get_db)
    ):
        self._db = db

    def get_users(
        self,
    ) -> List[UserSchema]:
        return self._db.query(UserSchema).all()

    def get_user_by_id(
        self,
        user_id: int
    ) -> UserSchema:
        return self._db.query(UserSchema).filter(UserSchema.id == user_id).first()

    def get_users_by_organization_id(
        self,
        organization_id: int
    ) -> List[UserSchema]:
        return self._db.query(UserSchema).filter(UserSchema.organization_id == organization_id).all()

    def create_user(
        self,
        user_data: UserRequest
    ) -> UserSchema:
        new_user = UserSchema(**user_data.model_dump())
        self._db.add(new_user)
        self._db.commit()
        self._db.refresh(new_user)
        return new_user
