"""empty message

Revision ID: f23f48bb9586
Revises: bcf3fb589109
Create Date: 2021-02-24 03:57:36.464072

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f23f48bb9586'
down_revision = 'bcf3fb589109'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todos', sa.Column('done', sa.Boolean(), nullable=False))
    op.add_column('todos', sa.Column('label', sa.String(length=120), nullable=False))
    op.drop_index('name', table_name='todos')
    op.create_unique_constraint(None, 'todos', ['label'])
    op.drop_column('todos', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todos', sa.Column('name', mysql.VARCHAR(length=120), nullable=False))
    op.drop_constraint(None, 'todos', type_='unique')
    op.create_index('name', 'todos', ['name'], unique=True)
    op.drop_column('todos', 'label')
    op.drop_column('todos', 'done')
    # ### end Alembic commands ###
