"""empty message

Revision ID: d5eec60bf8be
Revises: 
Create Date: 2019-04-11 18:51:29.246935

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd5eec60bf8be'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('LinRegResults',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('YearsExperience', sa.Float(), nullable=True),
    sa.Column('Prediction', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('LinRegResults')
    # ### end Alembic commands ###
