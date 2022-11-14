"""add language to posts

Revision ID: 8551a143efb1
Revises: 1ca271f6da69
Create Date: 2022-11-12 10:50:47.562054

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8551a143efb1'
down_revision = '1ca271f6da69'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('language', sa.String(length=5), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'language')
    # ### end Alembic commands ###
