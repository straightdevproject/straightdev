from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# SQL_ALQUEMY_DATABASE_URL = 'postgresql://postgres:mapajos2010@localhost/straightdev'
SQL_ALQUEMY_DATABASE_URL = f"postgresql://{os.environ['POSTGRES_USER']}:{os.environ['POSTGRES_PASSWORD']}@db/{os.environ['POSTGRES_DB']}"

engine = create_engine(SQL_ALQUEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()