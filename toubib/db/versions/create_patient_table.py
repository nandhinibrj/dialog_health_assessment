"""Add patient table

Revision ID: 002
Revises:
Create Date: 2021-06-02 14:31:33.813799

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "002"
down_revision = "001"
branch_labels = None
depends_on = None


def upgrade():
    # 🥸 This is where you add patient table.
    op.create_table(
        "patient",
        sa.Column(
            "id", sa.Integer, sa.Identity(always=True), nullable=False, primary_key=True
        ),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.current_timestamp(),
            nullable=False,
        ),
        sa.Column("first_name", sa.String, nullable=False),
        sa.Column("last_name", sa.String, nullable=False),
        sa.Column("email", sa.String, nullable=False),
        sa.Column("date_of_birth", sa.String, nullable=False),
        sa.Column("sex_at_birth", sa.String, nullable=False),
    )


def downgrade():
    # 🥸 This is where you drop it.
    pass
