"""add avatar_path to users

Revision ID: bfb1714bc3a3
Revises: 
Create Date: 2025-02-25 13:04:44.758099

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = 'bfb1714bc3a3'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    op.add_column('users', sa.Column('avatar_path', sa.String(), nullable=True))


def downgrade() -> None:
    op.drop_column('users', 'avatar_path')
