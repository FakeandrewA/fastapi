"""add last few columns to posts table

Revision ID: 81ec9d5ebee3
Revises: ea6ded50999b
Create Date: 2025-06-24 18:50:28.334711

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '81ec9d5ebee3'
down_revision: Union[str, Sequence[str], None] = 'ea6ded50999b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False,server_default='TRUE' ))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), 
                                     nullable=False, server_default=sa.text('NOW()')))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("posts","published")
    op.drop_column("posts","created_at")
    pass
