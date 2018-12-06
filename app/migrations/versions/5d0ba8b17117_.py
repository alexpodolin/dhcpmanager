"""empty message

Revision ID: 5d0ba8b17117
Revises: 
Create Date: 2018-12-03 10:45:34.975636

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d0ba8b17117'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hosts_allow',
    sa.Column('id', sa.SmallInteger(), nullable=False),
    sa.Column('hostname', sa.VARCHAR(length=32), nullable=False),
    sa.Column('mac_addr', sa.VARCHAR(length=18), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('mac_addr')
    )
    op.create_table('net_ipv4',
    sa.Column('id', sa.SmallInteger(), nullable=False),
    sa.Column('interface', sa.VARCHAR(length=15), nullable=False),
    sa.Column('subnet_ipv4', sa.VARCHAR(length=15), nullable=False),
    sa.Column('netmask', sa.VARCHAR(length=15), nullable=False),
    sa.Column('default_gw', sa.VARCHAR(length=15), nullable=False),
    sa.Column('broadcast', sa.VARCHAR(length=15), nullable=False),
    sa.Column('ip_range_start', sa.VARCHAR(length=15), nullable=False),
    sa.Column('ip_range_end', sa.VARCHAR(length=15), nullable=False),
    sa.Column('dns_suffix', sa.VARCHAR(length=20), server_default='nr.local', nullable=False),
    sa.Column('dns_srv_01', sa.VARCHAR(length=15), server_default='192.168.156.93', nullable=False),
    sa.Column('dns_srv_02', sa.VARCHAR(length=15), server_default='192.168.156.94', nullable=False),
    sa.Column('failover_peer', sa.VARCHAR(length=20), server_default='nr-dhcpd-failover', nullable=False),
    sa.Column('opt_242', sa.VARCHAR(length=150), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reserved_ipv4',
    sa.Column('id', sa.SmallInteger(), nullable=False),
    sa.Column('hostname', sa.VARCHAR(length=32), nullable=False),
    sa.Column('mac_addr', sa.VARCHAR(length=18), nullable=False),
    sa.Column('res_ipv4', sa.VARCHAR(length=15), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('res_ipv4')
    )
    op.create_table('user',
    sa.Column('id', sa.SmallInteger(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_table('reserved_ipv4')
    op.drop_table('net_ipv4')
    op.drop_table('hosts_allow')
    # ### end Alembic commands ###