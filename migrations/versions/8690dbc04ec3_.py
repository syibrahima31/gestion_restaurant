"""empty message

Revision ID: 8690dbc04ec3
Revises: 
Create Date: 2024-07-07 22:46:55.059489

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8690dbc04ec3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('menu',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nom', sa.String(), nullable=True),
    sa.Column('description', sa.String(length=300), nullable=True),
    sa.Column('prix', sa.Float(), nullable=True),
    sa.Column('disponibilite', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nom', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('role', sa.Integer(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('role')
    )
    op.create_table('commande',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('total', sa.String(), nullable=True),
    sa.Column('statut', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('plat',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nom', sa.String(), nullable=True),
    sa.Column('ingredients', sa.String(), nullable=True),
    sa.Column('prix', sa.Float(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('menu_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['menu_id'], ['menu.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('commande_plat',
    sa.Column('commande_id', sa.Integer(), nullable=True),
    sa.Column('plat_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['commande_id'], ['commande.id'], ),
    sa.ForeignKeyConstraint(['plat_id'], ['plat.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('commande_plat')
    op.drop_table('plat')
    op.drop_table('commande')
    op.drop_table('user')
    op.drop_table('menu')
    # ### end Alembic commands ###
