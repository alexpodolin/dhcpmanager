"""empty message

Revision ID: b7425e9d553f
Revises: 
Create Date: 2018-05-31 13:54:19.779976

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b7425e9d553f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('net_ipv4')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('net_ipv4',
    sa.Column('id', mysql.SMALLINT(display_width=6), nullable=False),
    sa.Column('interface', mysql.VARCHAR(length=15), nullable=False),
    sa.Column('subNetIpv4', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('netmask', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('default_gw', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('broadcast', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('ip_range_start', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('ip_range_end', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('failover_peer', mysql.VARCHAR(length=20), nullable=False),
    sa.Column('opt_242', mysql.VARCHAR(length=150), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###