from typing import List
from fastapi import FastAPI, Depends, HTTPException, status
from app import schemas
from app.database import get_db
from app.models import UserRequest, UserResponseWithOrganization, OrganizationResponse, OrganizationRequest, OrganizationUsers
from sqlalchemy.orm import Session

# schemas.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to my API"}


@app.get("/users", response_model=List[UserResponseWithOrganization])
def get_users(db: Session = Depends(get_db)):
    users = db.query(schemas.User).all()
    return users


@app.get("/users/{id}", response_model=UserResponseWithOrganization)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(schemas.User).filter(schemas.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {id} was not found")
    return user


@app.get("/users/organization/{organization_id}", response_model=OrganizationUsers)
def get_users_by_organization_id(organization_id: int, db: Session = Depends(get_db)):
    organization = db.query(schemas.Organization).filter(schemas.Organization.id == organization_id).first()
    if not organization:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"organization with id {organization_id} was not found")
    users = db.query(schemas.User).filter(schemas.User.organization_id == organization_id).all()
    return OrganizationUsers(organization=organization, users=users)


@app.post("/users", status_code=status.HTTP_201_CREATED, response_model=UserResponseWithOrganization)
def create_user(user: UserRequest, db: Session = Depends(get_db)):
    new_user = schemas.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.get("/organizations", response_model=List[OrganizationResponse])
def get_organizations(db: Session = Depends(get_db)):
    organizations = db.query(schemas.Organization).all()
    return organizations


@app.post("/organizations", status_code=status.HTTP_201_CREATED, response_model=OrganizationResponse)
def create_organization(organization: OrganizationRequest, db: Session = Depends(get_db)):
    new_organization = schemas.Organization(**organization.model_dump())
    db.add(new_organization)
    db.commit()
    db.refresh(new_organization)
    return new_organization
