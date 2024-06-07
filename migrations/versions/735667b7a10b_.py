"""empty message

Revision ID: 735667b7a10b
Revises: 85942c087556
Create Date: 2024-06-06 00:46:53.852347

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '735667b7a10b'
down_revision = '85942c087556'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('terrain', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('person', schema=None) as batch_op:
        batch_op.add_column(sa.Column('planet_residing', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'planet', ['planet_residing'], ['id'])
        batch_op.drop_column('height')
        batch_op.drop_column('mass')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('person', schema=None) as batch_op:
        batch_op.add_column(sa.Column('mass', sa.VARCHAR(length=250), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('height', sa.VARCHAR(length=250), autoincrement=False, nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('planet_residing')

    op.drop_table('planet')
    # ### end Alembic commands ###
