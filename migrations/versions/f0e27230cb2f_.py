"""empty message

Revision ID: f0e27230cb2f
Revises: 
Create Date: 2022-04-10 21:42:13.670576

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f0e27230cb2f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('branches',
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('city', sa.String(length=20), nullable=True),
    sa.Column('asset', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('name')
    )
    op.create_table('clients',
    sa.Column('id', sa.String(length=20), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.Column('phone', sa.String(length=15), nullable=True),
    sa.Column('address', sa.String(length=256), nullable=True),
    sa.Column('email', sa.String(length=30), nullable=True),
    sa.Column('contact_name', sa.String(length=20), nullable=True),
    sa.Column('contact_phone', sa.String(length=15), nullable=True),
    sa.Column('contact_email', sa.String(length=30), nullable=True),
    sa.Column('contact_relation', sa.String(length=40), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('system_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('branchrecords',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('branch_name', sa.String(length=100), nullable=True),
    sa.Column('OpType', sa.String(length=4), nullable=True),
    sa.Column('OpTime', sa.DateTime(), nullable=True),
    sa.Column('OpMoney', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['branch_name'], ['branches.name'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('employees',
    sa.Column('id', sa.String(length=20), nullable=False),
    sa.Column('branch_name', sa.String(length=100), nullable=True),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.Column('phone', sa.String(length=15), nullable=True),
    sa.Column('address', sa.String(length=256), nullable=True),
    sa.Column('enroll_date', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['branch_name'], ['branches.name'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('checks',
    sa.Column('id', sa.String(length=20), nullable=False),
    sa.Column('branch_name', sa.String(length=100), nullable=True),
    sa.Column('employee_id', sa.String(length=20), nullable=True),
    sa.Column('balance', sa.Float(), nullable=True),
    sa.Column('open_date', sa.DateTime(), nullable=True),
    sa.Column('over_draft', sa.Float(), nullable=True),
    sa.Column('last_access_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['branch_name'], ['branches.name'], ),
    sa.ForeignKeyConstraint(['employee_id'], ['employees.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('loans',
    sa.Column('id', sa.String(length=20), nullable=False),
    sa.Column('branch_name', sa.String(length=100), nullable=True),
    sa.Column('employee_id', sa.String(length=20), nullable=True),
    sa.Column('amount', sa.Float(), nullable=True),
    sa.Column('status', sa.String(length=20), nullable=True),
    sa.ForeignKeyConstraint(['branch_name'], ['branches.name'], ),
    sa.ForeignKeyConstraint(['employee_id'], ['employees.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('savings',
    sa.Column('id', sa.String(length=20), nullable=False),
    sa.Column('branch_name', sa.String(length=100), nullable=True),
    sa.Column('employee_id', sa.String(length=20), nullable=True),
    sa.Column('balance', sa.Float(), nullable=True),
    sa.Column('open_date', sa.DateTime(), nullable=True),
    sa.Column('interest_rate', sa.String(length=10), nullable=True),
    sa.Column('currency_type', sa.String(length=5), nullable=True),
    sa.Column('last_access_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['branch_name'], ['branches.name'], ),
    sa.ForeignKeyConstraint(['employee_id'], ['employees.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('checkconstraint',
    sa.Column('client_id', sa.String(length=20), nullable=False),
    sa.Column('branch_name', sa.String(length=100), nullable=False),
    sa.Column('check_id', sa.String(length=20), nullable=False),
    sa.ForeignKeyConstraint(['branch_name'], ['branches.name'], ),
    sa.ForeignKeyConstraint(['check_id'], ['savings.id'], ),
    sa.ForeignKeyConstraint(['client_id'], ['clients.id'], ),
    sa.PrimaryKeyConstraint('client_id', 'branch_name', 'check_id'),
    sa.UniqueConstraint('client_id', 'branch_name', name='con1')
    )
    op.create_table('clientchecks',
    sa.Column('client_id', sa.String(length=20), nullable=False),
    sa.Column('check_id', sa.String(length=20), nullable=False),
    sa.ForeignKeyConstraint(['check_id'], ['checks.id'], ),
    sa.ForeignKeyConstraint(['client_id'], ['clients.id'], ),
    sa.PrimaryKeyConstraint('client_id', 'check_id')
    )
    op.create_table('clientsavings',
    sa.Column('client_id', sa.String(length=20), nullable=False),
    sa.Column('saving_id', sa.String(length=20), nullable=False),
    sa.ForeignKeyConstraint(['client_id'], ['clients.id'], ),
    sa.ForeignKeyConstraint(['saving_id'], ['savings.id'], ),
    sa.PrimaryKeyConstraint('client_id', 'saving_id')
    )
    op.create_table('hasloans',
    sa.Column('client_id', sa.String(length=20), nullable=False),
    sa.Column('loan_id', sa.String(length=20), nullable=False),
    sa.ForeignKeyConstraint(['client_id'], ['clients.id'], ),
    sa.ForeignKeyConstraint(['loan_id'], ['loans.id'], ),
    sa.PrimaryKeyConstraint('client_id', 'loan_id')
    )
    op.create_table('loanlogs',
    sa.Column('id', sa.String(length=30), nullable=False),
    sa.Column('loan_id', sa.String(length=20), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('amount', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['loan_id'], ['loans.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('savingconstraints',
    sa.Column('client_id', sa.String(length=20), nullable=False),
    sa.Column('branch_name', sa.String(length=100), nullable=False),
    sa.Column('saving_id', sa.String(length=20), nullable=False),
    sa.ForeignKeyConstraint(['branch_name'], ['branches.name'], ),
    sa.ForeignKeyConstraint(['client_id'], ['clients.id'], ),
    sa.ForeignKeyConstraint(['saving_id'], ['savings.id'], ),
    sa.PrimaryKeyConstraint('client_id', 'branch_name', 'saving_id'),
    sa.UniqueConstraint('client_id', 'branch_name', name='con1')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('savingconstraints')
    op.drop_table('loanlogs')
    op.drop_table('hasloans')
    op.drop_table('clientsavings')
    op.drop_table('clientchecks')
    op.drop_table('checkconstraint')
    op.drop_table('savings')
    op.drop_table('loans')
    op.drop_table('checks')
    op.drop_table('employees')
    op.drop_table('branchrecords')
    op.drop_table('system_user')
    op.drop_table('clients')
    op.drop_table('branches')
    # ### end Alembic commands ###