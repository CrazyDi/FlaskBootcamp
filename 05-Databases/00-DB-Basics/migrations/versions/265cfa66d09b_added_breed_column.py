"""added breed column

Revision ID: 265cfa66d09b
Revises: 
Create Date: 2020-06-03 14:44:47.693125

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '265cfa66d09b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('puppies', sa.Column('breed', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('puppies', 'breed')
    # ### end Alembic commands ###
