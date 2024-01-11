"""Create Organizations table

Revision ID: b2be7576c859
Revises: 
Create Date: 2024-01-11 15:50:02.598239

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b2be7576c859'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("organizations", sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
                    sa.Column("name", sa.String(), nullable=False),
                    sa.Column("created_at", sa.TIMESTAMP(), nullable=False, server_default=sa.text("now()")))
    pass


def downgrade() -> None:
    op.drop_table("organizations")
    pass
