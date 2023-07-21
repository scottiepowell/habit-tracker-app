# upgrade.py
from alembic import op
import sqlalchemy as sa
from sqlalchemy import text

def upgrade():
    # create temporary _user table
    op.create_table(
        '_user',
        sa.Column('user_id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String(64), unique=True, nullable=False),
        sa.Column('password_hash', sa.String(128), nullable=False),
        sa.Column('username', sa.String(64), unique=True, nullable=False, server_default="user00001")
    )

    op.execute("""
        INSERT INTO _user (user_id, email, password_hash, username)
        SELECT user_id, email, password_hash, "user00001" FROM user;
    """)

    # drop old user table
    op.drop_table('user')

    # rename temporary _user to user
    op.rename_table('_user', 'user')
