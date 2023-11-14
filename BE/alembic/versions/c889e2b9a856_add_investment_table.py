"""Add investment table

Revision ID: c889e2b9a856
Revises: addf12d8324d
Create Date: 2023-11-14 00:17:21.283763

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c889e2b9a856'
down_revision: Union[str, None] = 'addf12d8324d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # commands to create the Investment table
    op.create_table(
        'investments',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('platform_id', sa.String(length=100), nullable=True),
        sa.Column('invest_type', sa.String(length=50), nullable=True),
        sa.Column('name', sa.String(length=100), nullable=True),
        sa.Column('invested_time', sa.DateTime(), nullable=True),
        sa.Column('annual_return_rate', sa.Float(), nullable=True),
        sa.Column('expected_xor', sa.Float(), nullable=True),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    # commands to drop the Investment table
    op.drop_table('investments')