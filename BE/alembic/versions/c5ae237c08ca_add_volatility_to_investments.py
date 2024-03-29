"""Add volatility to investments

Revision ID: c5ae237c08ca
Revises: c889e2b9a856
Create Date: 2023-11-14 13:01:56.381874

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'c5ae237c08ca'
down_revision: Union[str, None] = 'c889e2b9a856'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('investments', sa.Column('volatility', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('investments', 'volatility')
