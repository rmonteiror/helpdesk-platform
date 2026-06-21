"""add_sla_fields

Revision ID: 2075d2953034
Revises: 2c9f2ce95238
Create Date: 2026-06-20 11:53:14.170727

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2075d2953034'
down_revision: Union[str, Sequence[str], None] = '2c9f2ce95238'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        'tickets',
        sa.Column(
            'sla_due_date',
            sa.DateTime(),
            nullable=True
        )
    )

    op.add_column(
        'tickets',
        sa.Column(
            'sla_status',
            sa.String(),
            nullable=False,
            server_default='on_time'
        )
    )


def downgrade() -> None:
    op.drop_column(
        'tickets',
        'sla_status'
    )

    op.drop_column(
        'tickets',
        'sla_due_date'
    )