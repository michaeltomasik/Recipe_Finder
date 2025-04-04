"""Recreate all tables

Revision ID: 42ed16406b89
Revises: 31271183ed71
Create Date: 2025-03-31 16:00:56.170986
"""

from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

revision: str = '42ed16406b89'
down_revision: Union[str, None] = '31271183ed71'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('username', sa.String(50), nullable=False, unique=True),
        sa.Column('email', sa.String(100), nullable=False, unique=True),
        sa.Column('password_hash', sa.String(255), nullable=False),
        sa.Column('avatar_path', sa.String(255), nullable=True),
    )

    op.create_table(
        'recipes',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('created_at', sa.DateTime(), default=sa.func.current_timestamp()),
    )

    op.create_table(
        'ingredients',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(100), nullable=False),
    )

    op.create_table(
        'recipe_ingredients',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('recipe_id', sa.Integer(), sa.ForeignKey('recipes.id', ondelete="CASCADE"), nullable=False),
        sa.Column('ingredient_id', sa.Integer(), sa.ForeignKey('ingredients.id', ondelete="CASCADE"), nullable=False),
        sa.Column('quantity', sa.String(50), nullable=True),  # Menge der Zutat (optional)
    )

    op.create_table(
        'dietary_preferences',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),  # Name der Diät (z.B. "vegetarisch")
    )

    op.create_table(
        'user_dietary_preferences',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id', ondelete="CASCADE"), nullable=False),
        sa.Column('dietary_preference_id', sa.Integer(), sa.ForeignKey('dietary_preferences.id', ondelete="CASCADE"), nullable=False),
    )

    op.create_table(
        'recipe_ratings',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('recipe_id', sa.Integer(), sa.ForeignKey('recipes.id', ondelete="CASCADE"), nullable=False),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id', ondelete="CASCADE"), nullable=False),
        sa.Column('rating', sa.Integer(), nullable=False),  # Bewertung (1-5)
        sa.Column('comment', sa.Text(), nullable=True),  # Kommentar zur Bewertung
    )

    op.create_table(
        'user_recipes',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id', ondelete="CASCADE"), nullable=False),
        sa.Column('recipe_id', sa.Integer(), sa.ForeignKey('recipes.id', ondelete="CASCADE"), nullable=False),
        sa.Column('is_favorite', sa.Boolean(), default=False),  # Markiert, ob das Rezept ein Favorit ist
    )


def downgrade() -> None:
    op.drop_table('user_recipes')
    op.drop_table('recipe_ratings')
    op.drop_table('user_dietary_preferences')
    op.drop_table('dietary_preferences')
    op.drop_table('recipe_ingredients')
    op.drop_table('ingredients')
    op.drop_table('recipes')
    op.drop_table('users')