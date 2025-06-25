"""add foreign key to post table

Revision ID: ea6ded50999b
Revises: bfb9261fcf08
Create Date: 2025-06-24 18:44:52.843691

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ea6ded50999b'
down_revision: Union[str, Sequence[str], None] = 'bfb9261fcf08'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts',sa.Column('user_id',sa.Integer(),nullable=False))
    op.create_foreign_key("posts_users_fk",
                          source_table="posts",
                          referent_table="users",local_cols=["user_id"],remote_cols=["id"],ondelete="CASCADE")
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint("posts_users_fk",table_name="posts")
    op.drop_column("posts","user_id")
