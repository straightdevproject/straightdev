"""Add surname column to users

Revision ID: 20c5bfa09e2f
Revises: b2be7576c859
Create Date: 2024-01-11 17:38:36.932291

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '20c5bfa09e2f'
down_revision: Union[str, None] = 'b2be7576c859'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('users', sa.Column('surname', sa.String(), nullable=False))


def downgrade():
    op.drop_column('users', 'surname')
