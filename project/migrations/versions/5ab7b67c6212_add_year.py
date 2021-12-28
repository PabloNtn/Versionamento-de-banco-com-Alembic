"""add year

Revision ID: 5ab7b67c6212
Revises: 6176d953e97a
Create Date: 2021-12-28 17:36:27.339555

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ab7b67c6212'
down_revision = '6176d953e97a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('song', sa.Column('year', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_song_year'), 'song', ['year'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_song_year'), table_name='song')
    op.drop_column('song', 'year')
    # ### end Alembic commands ###