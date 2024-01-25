"""ADD SURNAME COLUMN TO USERS TABLE

Revision ID: d11001d1d1b6
Revises: 4fb01beb1ee3
Create Date: 2024-01-25 13:44:46.134555

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd11001d1d1b6'
down_revision: Union[str, None] = '4fb01beb1ee3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('surname', sa.String(), nullable=True))


def downgrade() -> None:
    op.drop_column('users', 'surname')
