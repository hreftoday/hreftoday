"""remove issue

Revision ID: 81a76b1112b2
Revises: b7c2dae226b6
Create Date: 2016-02-04 20:33:12.029919

"""

# revision identifiers, used by Alembic.
revision = '81a76b1112b2'
down_revision = 'b7c2dae226b6'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('link', sa.Column('topic_id', sa.Integer(), nullable=True))
    op.drop_index('ix_issue', table_name='link')
    op.drop_constraint(u'fk_link_issue', 'link', type_='foreignkey')
    op.create_foreign_key('fk_link_topic', 'link', 'topic', ['topic_id'], ['id'])
    op.drop_column('link', 'issue_id')
    op.drop_table('issue')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('issue',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('topic_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('serial', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('published_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('title', sa.VARCHAR(length=128), server_default=sa.text(u"''::character varying"), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['topic_id'], [u'topic.id'], name=u'fk_issue_topic'),
    sa.ForeignKeyConstraint(['user_id'], [u'user.id'], name=u'fk_issue_user'),
    sa.PrimaryKeyConstraint('id', name=u'issue_pkey'),
    sa.UniqueConstraint('topic_id', 'serial', name=u'ux_issue_topic_serial')
    )
    op.add_column('link', sa.Column('issue_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint('fk_link_topic', 'link', type_='foreignkey')
    op.create_foreign_key(u'fk_link_issue', 'link', 'issue', ['issue_id'], ['id'])
    op.create_index('ix_issue', 'link', ['issue_id'], unique=False)
    op.drop_column('link', 'topic_id')
    ### end Alembic commands ###