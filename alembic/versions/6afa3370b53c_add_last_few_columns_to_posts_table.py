"""add last few columns to posts table

Revision ID: 6afa3370b53c
Revises: 7c8f45288dd4
Create Date: 2022-03-23 12:11:48.509329

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6afa3370b53c'
down_revision = '7c8f45288dd4'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default="TRUE"),)
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False,
                                     server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts', 'published')
    pass
