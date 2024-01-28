"""MAKE ORGANIZATION_ID COLUMN NOT NULLABLE

Revision ID: 443ee4bcd05d
Revises: c8861fbc1c6c
Create Date: 2024-01-28 15:53:08.716979

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '443ee4bcd05d'
down_revision: Union[str, None] = 'c8861fbc1c6c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('users', 'organization_id', nullable=False)
    pass


def downgrade() -> None:
    pass
