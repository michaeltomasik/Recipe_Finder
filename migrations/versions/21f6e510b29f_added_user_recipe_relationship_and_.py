"""Added User-Recipe relationship and dietary preferences

Revision ID: 21f6e510b29f
Revises: bfb1714bc3a3
Create Date: 2025-03-10 10:44:44.018293

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '21f6e510b29f'
down_revision: Union[str, None] = 'bfb1714bc3a3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
