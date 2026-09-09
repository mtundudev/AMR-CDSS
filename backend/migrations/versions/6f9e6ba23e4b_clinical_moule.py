"""clinical moule

Revision ID: 6f9e6ba23e4b
Revises: dc6f7656a974
Create Date: 2026-09-09 11:56:13.846182

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6f9e6ba23e4b'
down_revision: Union[str, Sequence[str], None] = 'dc6f7656a974'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
