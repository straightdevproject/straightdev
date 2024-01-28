"""ADD ORGANIZATION_ID COLUMN TO USERS TABLE

Revision ID: c8861fbc1c6c
Revises: d81605e697e2
Create Date: 2024-01-27 12:57:48.590433

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c8861fbc1c6c'
down_revision: Union[str, None] = 'd81605e697e2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Add organization_id column to the users table
    op.add_column('users', sa.Column('organization_id', sa.Integer(), nullable=True))


def downgrade():
    # Remove the organization_id column from the users table
    op.drop_column('users', 'organization_id')
