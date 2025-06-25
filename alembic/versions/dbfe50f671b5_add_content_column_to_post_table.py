"""add content column to post table

Revision ID: dbfe50f671b5
Revises: 73e316d4edc8
Create Date: 2025-06-24 18:33:02.670171

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dbfe50f671b5'
down_revision: Union[str, Sequence[str], None] = '73e316d4edc8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts','content')
    pass
