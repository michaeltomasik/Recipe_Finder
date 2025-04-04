"""Create ingredients table

Revision ID: 31271183ed71
Revises: e34dbec2ff7b
Create Date: 2025-03-31 15:57:58.979363

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '31271183ed71'
down_revision: Union[str, None] = 'e34dbec2ff7b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
