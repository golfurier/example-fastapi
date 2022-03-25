"""add foreign-key to posts table

Revision ID: 7c8f45288dd4
Revises: 572e971f334a
Create Date: 2022-03-23 12:00:25.966905

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c8f45288dd4'
down_revision = '572e971f334a'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", 
                           local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('post', 'owner_id')
    pass
