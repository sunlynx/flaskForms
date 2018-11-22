"""empty message

Revision ID: 82c881bc84ac
Revises: 
Create Date: 2018-11-18 18:24:19.556557

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '82c881bc84ac'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('idUser', sa.Integer(), nullable=False),
    sa.Column('login', sa.String(length=80), nullable=True),
    sa.Column('mail', sa.String(length=120), nullable=True),
    sa.Column('paswd', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('idUser'),
    sa.UniqueConstraint('login'),
    sa.UniqueConstraint('mail')
    )
    op.create_table('surveys',
    sa.Column('idSurvey', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('desc', sa.Text(), nullable=True),
    sa.Column('idUser', sa.Integer(), nullable=True),
    sa.Column('isActive', sa.Boolean(), nullable=True),
    sa.Column('subCount', sa.Integer(), nullable=True),
    sa.Column('dueDate', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['idUser'], ['users.idUser'], ),
    sa.PrimaryKeyConstraint('idSurvey'),
    sa.UniqueConstraint('name')
    )
    op.create_table('questions',
    sa.Column('idQuestion', sa.Integer(), nullable=False),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('type', sa.String(length=50), nullable=True),
    sa.Column('idSurvey', sa.Integer(), nullable=True),
    sa.Column('replyContent', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['idSurvey'], ['surveys.idSurvey'], ),
    sa.PrimaryKeyConstraint('idQuestion')
    )
    op.create_table('replies',
    sa.Column('idReply', sa.Integer(), nullable=False),
    sa.Column('idQuestion', sa.Integer(), nullable=True),
    sa.Column('reply', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['idQuestion'], ['questions.idQuestion'], ),
    sa.PrimaryKeyConstraint('idReply')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('replies')
    op.drop_table('questions')
    op.drop_table('surveys')
    op.drop_table('users')
    # ### end Alembic commands ###