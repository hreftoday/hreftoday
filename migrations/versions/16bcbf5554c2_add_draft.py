"""add draft

Revision ID: 16bcbf5554c2
Revises: 674bb6602f02
Create Date: 2016-02-26 18:30:59.126832

"""

# revision identifiers, used by Alembic.
revision = '16bcbf5554c2'
down_revision = '674bb6602f02'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('draft',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('link_ids', postgresql.ARRAY(sa.Integer()), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id', name='ux_draft_user')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('draft')
    ### end Alembic commands ###
