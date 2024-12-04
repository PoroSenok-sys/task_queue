"""update type date on datetime

Revision ID: 58508b91c6c3
Revises: 2e9bea35f698
Create Date: 2024-12-04 12:17:25.577683

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '58508b91c6c3'
down_revision: Union[str, None] = '2e9bea35f698'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('task', 'create_time',
               existing_type=sa.DATE(),
               type_=sa.DateTime(),
               existing_nullable=False)
    op.alter_column('task', 'start_time',
               existing_type=sa.DATE(),
               type_=sa.DateTime(),
               existing_nullable=True)
    op.alter_column('task', 'exec_time',
               existing_type=sa.DATE(),
               type_=sa.DateTime(),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('task', 'exec_time',
               existing_type=sa.DateTime(),
               type_=sa.DATE(),
               existing_nullable=True)
    op.alter_column('task', 'start_time',
               existing_type=sa.DateTime(),
               type_=sa.DATE(),
               existing_nullable=True)
    op.alter_column('task', 'create_time',
               existing_type=sa.DateTime(),
               type_=sa.DATE(),
               existing_nullable=False)
    # ### end Alembic commands ###
