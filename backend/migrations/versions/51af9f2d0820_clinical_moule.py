"""clinical moule

Revision ID: 51af9f2d0820
Revises: 6f9e6ba23e4b
Create Date: 2026-09-09 16:27:11.009161

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '51af9f2d0820'
down_revision: Union[str, Sequence[str], None] = '6f9e6ba23e4b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
