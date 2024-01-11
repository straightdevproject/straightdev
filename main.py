from fastapi import FastAPI, Depends, HTTPException, status
from app import schemas
from app.database import engine, get_db
from app.models import OrganizationResponse, UserRequest, UserResponse, OrganizationRequest
from sqlalchemy.orm import Session

schemas.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to my API"}

@app.get("/users/{id}", response_model=UserResponse)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(schemas.User).filter(schemas.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {id} was not found")
    return user

@app.post("/users", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
def create_user(user: UserRequest, db: Session = Depends(get_db)):
    new_user = schemas.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get("/organizations/{id}", response_model=OrganizationResponse)
def get_organization(id: int, db: Session = Depends(get_db)):
    organization = db.query(schemas.Organization).filter(schemas.Organization.id == id).first()
    if not organization:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Organization with id {id} was not found")
    return organization

@app.post("/organizations", status_code=status.HTTP_201_CREATED, response_model=OrganizationResponse)
def create_organization(organization: OrganizationRequest, db: Session = Depends(get_db)):
    new_organization = schemas.Organization(**organization.dict())
    db.add(new_organization)
    db.commit()
    db.refresh(new_organization)
    return new_organization
