"""empty message

Revision ID: 20d982e97e89
Revises: 
Create Date: 2019-10-10 17:00:37.575193

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20d982e97e89'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('barber',
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=False),
    sa.Column('last_name', sa.String(length=50), nullable=False),
    sa.Column('password', sa.Text(), nullable=False),
    sa.Column('status', sa.String(length=12), nullable=True),
    sa.PrimaryKeyConstraint('email')
    )
    op.create_table('service',
    sa.Column('service_id', sa.Integer(), nullable=False),
    sa.Column('customer', sa.String(length=50), nullable=False),
    sa.Column('location', sa.Text(), nullable=False),
    sa.Column('barber', sa.String(), nullable=False),
    sa.Column('start', sa.DateTime(), nullable=False),
    sa.Column('stop', sa.DateTime(), nullable=True),
    sa.Column('duration', sa.Integer(), nullable=True),
    sa.Column('fee', sa.String(length=12), nullable=True),
    sa.Column('status', sa.String(length=12), nullable=True),
    sa.ForeignKeyConstraint(['barber'], ['barber.email'], ),
    sa.PrimaryKeyConstraint('service_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('service')
    op.drop_table('barber')
    # ### end Alembic commands ###
