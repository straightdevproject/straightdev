from sqlalchemy.orm import Session
from app.domain.repositories_interfaces.organization_repository_interface import OrganizationRepositoryInterface
from app.infrastructure.schemas.organization import Organization as OrganizationSchema
from fastapi import Depends
from app.infrastructure.database.database import get_db
from app.domain.models.organization import OrganizationRequest
from typing import List


class OrganizationRepository(OrganizationRepositoryInterface):

    def __init__(
            self,
            db: Session = Depends(get_db)
    ):
        self._db = db

    def get_organizations(
        self,
    ) -> List[OrganizationSchema]:
        return self._db.query(OrganizationSchema).all()

    def get_organization_by_id(
        self,
        id: int
    ) -> OrganizationSchema:
        return self._db.query(OrganizationSchema).filter(OrganizationSchema.id == id).first()

    def get_organization_by_name(
        self,
        name: str
    ) -> OrganizationSchema:
        return self._db.query(OrganizationSchema).filter(OrganizationSchema.name == name).first()

    def create_organization(
        self,
        organization_data: OrganizationRequest
    ) -> OrganizationSchema:
        new_organization = OrganizationSchema(**organization_data.model_dump())
        self._db.add(new_organization)
        self._db.commit()
        self._db.refresh(new_organization)
        return new_organization
