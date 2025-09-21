"""Creating Database

Revision ID: e11313fb34aa
Revises: 83a77e8f1c84
Create Date: 2025-09-19 13:48:12.273547

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e11313fb34aa'
down_revision: Union[str, Sequence[str], None] = '83a77e8f1c84'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
