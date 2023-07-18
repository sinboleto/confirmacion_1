"""Update Information model

Revision ID: 05dbfcfc6825
Revises: 8f64b999a68f
Create Date: 2023-07-18 13:08:16.349737

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '05dbfcfc6825'
down_revision = '8f64b999a68f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('information', schema=None) as batch_op:
        batch_op.add_column(sa.Column('phone_number', sa.String(length=20), nullable=False))
        batch_op.add_column(sa.Column('question', sa.String(length=500), nullable=False))
        batch_op.add_column(sa.Column('answer', sa.String(length=500), nullable=False))
        batch_op.drop_column('info')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('information', schema=None) as batch_op:
        batch_op.add_column(sa.Column('info', sa.VARCHAR(length=500), nullable=False))
        batch_op.drop_column('answer')
        batch_op.drop_column('question')
        batch_op.drop_column('phone_number')

    # ### end Alembic commands ###