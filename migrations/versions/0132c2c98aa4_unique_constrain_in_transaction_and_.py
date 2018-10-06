"""Unique constrain in transaction and timezone in date columns

Revision ID: 0132c2c98aa4
Revises: dba57cf901e1
Create Date: 2018-10-06 03:01:21.645291

"""
import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = '0132c2c98aa4'
down_revision = 'dba57cf901e1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'transactions', ['orden_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'transactions', type_='unique')
    # ### end Alembic commands ###
