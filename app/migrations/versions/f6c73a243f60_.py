"""empty message

Revision ID: f6c73a243f60
Revises: ec6055fb506b
Create Date: 2018-09-12 10:58:12.236640

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f6c73a243f60'
down_revision = 'ec6055fb506b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('net_ipv4', sa.Column('opt_242', sa.VARCHAR(length=150), nullable=True))
    op.drop_column('net_ipv4', 'vlan_num')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('net_ipv4', sa.Column('vlan_num', mysql.VARCHAR(length=150), nullable=True))
    op.drop_column('net_ipv4', 'opt_242')
    # ### end Alembic commands ###
