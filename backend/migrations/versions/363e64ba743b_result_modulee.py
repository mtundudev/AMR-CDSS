"""result modulee

Revision ID: 363e64ba743b
Revises: 5eaa8cf73d64
Create Date: 2026-09-09 16:41:25.470986

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '363e64ba743b'
down_revision: Union[str, Sequence[str], None] = '5eaa8cf73d64'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'analysis_results',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('visit_id', sa.Integer(), nullable=False),
        sa.Column('pathogen_id', sa.Integer(), nullable=True),
        sa.Column('image_path', sa.String(length=255), nullable=False),
        sa.Column('confidence_score', sa.Float(), nullable=True),
        sa.Column('detection_summary', sa.Text(), nullable=True),
        sa.Column('analyzed_at', sa.DateTime(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(['pathogen_id'], ['pathogens.id']),
        sa.ForeignKeyConstraint(['visit_id'], ['clinical_visits.id']),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_index(op.f('ix_analysis_results_id'), 'analysis_results', ['id'], unique=False)
    op.create_index(op.f('ix_analysis_results_visit_id'), 'analysis_results', ['visit_id'], unique=False)


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index(op.f('ix_analysis_results_visit_id'), table_name='analysis_results')
    op.drop_index(op.f('ix_analysis_results_id'), table_name='analysis_results')
    op.drop_table('analysis_results')
