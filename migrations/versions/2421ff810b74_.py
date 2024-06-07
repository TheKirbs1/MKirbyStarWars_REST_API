"""empty message

Revision ID: 2421ff810b74
Revises: 
Create Date: 2024-06-05 23:58:27.690226

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2421ff810b74'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('person',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('homeworld', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('person')
    # ### end Alembic commands ###