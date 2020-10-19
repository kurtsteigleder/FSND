"""empty message

Revision ID: 332428c0ac20
Revises: c1d3f5237ba7
Create Date: 2020-10-18 20:52:02.191870

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '332428c0ac20'
down_revision = 'c1d3f5237ba7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('show',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('start_time', sa.DateTime(), nullable=True),
    sa.Column('venue_id', sa.Integer(), nullable=False),
    sa.Column('venue_name', sa.String(), nullable=True),
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.Column('artist_name', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['artist_id'], ['artist.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['venue_id'], ['venue.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('show')
    # ### end Alembic commands ###