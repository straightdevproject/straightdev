from sqlalchemy.orm import relationship

from app.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    organization_id = Column(Integer, ForeignKey('organizations.id'))
    organization = relationship('Organization', back_populates='users')


class Organization(Base):
    __tablename__ = "organizations"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    users = relationship('User', back_populates='organization')
