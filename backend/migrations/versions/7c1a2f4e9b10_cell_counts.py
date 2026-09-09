"""create cell counts table

Revision ID: 7c1a2f4e9b10
Revises: 363e64ba743b
Create Date: 2026-09-09

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '7c1a2f4e9b10'
down_revision: Union[str, Sequence[str], None] = '363e64ba743b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'cell_counts',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('analysis_result_id', sa.Integer(), nullable=False),
        sa.Column('rbc_count', sa.Float(), nullable=True),
        sa.Column('wbc_count', sa.Float(), nullable=True),
        sa.Column('platelet_count', sa.Float(), nullable=True),
        sa.Column('hemoglobin_level', sa.Float(), nullable=True),
        sa.Column('hematocrit', sa.Float(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(['analysis_result_id'], ['analysis_results.id']),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_index(op.f('ix_cell_counts_id'), 'cell_counts', ['id'], unique=False)


def downgrade() -> None:
    op.drop_index(op.f('ix_cell_counts_id'), table_name='cell_counts')
    op.drop_table('cell_counts')