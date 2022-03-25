"""add user table

Revision ID: 572e971f334a
Revises: e2898a11731b
Create Date: 2022-03-23 11:38:58.473277

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '572e971f334a'
down_revision = 'e2898a11731b'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa. Integer (), nullable=False) ,
                    sa.Column ( 'email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created at', sa. TIMESTAMP (timezone=True),
                                server_default=sa.text ('now()'), nullable=False),
                    sa.PrimaryKeyConstraint ('id'),
                    sa.UniqueConstraint('email')
)
    pass


def downgrade():
    op.drop_table('users')
    pass
