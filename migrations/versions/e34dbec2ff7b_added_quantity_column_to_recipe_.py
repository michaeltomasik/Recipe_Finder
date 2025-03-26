"""Added quantity column to recipe_ingredients table

Revision ID: e34dbec2ff7b
Revises: 21f6e510b29f
Create Date: 2025-03-26 12:32:13.243736

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e34dbec2ff7b'
down_revision: Union[str, None] = '21f6e510b29f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
