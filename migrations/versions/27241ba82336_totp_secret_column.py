"""totp_secret column

Revision ID: 27241ba82336
Revises: 
Create Date: 2023-07-11 17:49:08.393272

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '27241ba82336'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('totp_secret', sa.String(length=16), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('totp_secret')

    # ### end Alembic commands ###