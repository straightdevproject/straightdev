from typing import List
from fastapi import FastAPI, Depends, status
from app.infrastructure.schemas.organization import Organization as OrganizationSchema
from app.infrastructure.database.database import get_db
from app.domain.models.organization import OrganizationRequest, OrganizationResponse
from sqlalchemy.orm import Session
from app.infrastructure.controllers import user_controller
from app.infrastructure.controllers import organization_controller

# schemas.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(user_controller.router)
app.include_router(organization_controller.router)


@app.get("/")
async def root():
    return {"message": "Welcome to my API"}


# @app.get("/users", response_model=List[UserResponseOrganization])
# def get_users(db: Session = Depends(get_db)):
#     users = db.query(UserSchema).all()
#     return users
#
#
# @app.get("/users/{id}", response_model=UserResponseOrganization)
# def get_user(id: int, db: Session = Depends(get_db)):
#     user = db.query(UserSchema).filter(UserSchema.id == id).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"User with id {id} was not found")
#     return user
#
#
# @app.get("/users/organization/{organization_id}", response_model=OrganizationUsers)
# def get_users_by_organization_id(organization_id: int, db: Session = Depends(get_db)):
#     organization = db.query(OrganizationSchema).filter(OrganizationSchema.id == organization_id).first()
#     if not organization:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"organization with id {organization_id} was not found")
#     users = db.query(UserSchema).filter(UserSchema.organization_id == organization_id).all()
#     return OrganizationUsers(organization=organization, users=users)
#
#
# @app.post("/users", status_code=status.HTTP_201_CREATED, response_model=UserResponseOrganization)
# def create_user(user: UserRequest, db: Session = Depends(get_db)):
#     new_user = UserSchema(**user.model_dump())
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user


# @app.get("/organizations", response_model=List[OrganizationResponse])
# def get_organizations(db: Session = Depends(get_db)):
#     organizations = db.query(OrganizationSchema).all()
#     return organizations
#
#
# @app.post("/organizations", status_code=status.HTTP_201_CREATED, response_model=OrganizationResponse)
# def create_organization(organization: OrganizationRequest, db: Session = Depends(get_db)):
#     new_organization = OrganizationSchema(**organization.model_dump())
#     db.add(new_organization)
#     db.commit()
#     db.refresh(new_organization)
#     return new_organization
