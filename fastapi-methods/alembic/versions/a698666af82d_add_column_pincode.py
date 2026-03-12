"""add column pincode

Revision ID: a698666af82d
Revises: 
Create Date: 2026-03-11 18:04:51.479882

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a698666af82d'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None



def upgrade() -> None:
    op.add_column('product', sa.Column('pincode',sa.Integer))

    


def downgrade() -> None:
    """Downgrade schema."""
    pass
