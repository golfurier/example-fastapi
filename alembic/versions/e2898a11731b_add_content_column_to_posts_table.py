"""add content column to posts table

Revision ID: e2898a11731b
Revises: 0b8f2b120c31
Create Date: 2022-03-23 11:31:54.322290

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e2898a11731b'
down_revision = '0b8f2b120c31'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
