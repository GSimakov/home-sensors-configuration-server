"""init

Revision ID: 96f67d2404d5
Revises: 
Create Date: 2024-03-28 12:45:40.415194

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision: str = '96f67d2404d5'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Board',
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('description', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_Board_id'), 'Board', ['id'], unique=False)
    op.create_table('MeasurementType',
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('unit', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_MeasurementType_id'), 'MeasurementType', ['id'], unique=False)
    op.create_table('Transmitter',
    sa.Column('IP', sqlalchemy_utils.types.ip_address.IPAddressType(length=50), nullable=False),
    sa.Column('MAC', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_Transmitter_id'), 'Transmitter', ['id'], unique=False)
    op.create_table('Sensor',
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('type', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('measurement_type_id', sqlmodel.sql.sqltypes.GUID(), nullable=True),
    sa.Column('id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['measurement_type_id'], ['MeasurementType.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_Sensor_id'), 'Sensor', ['id'], unique=False)
    op.create_table('DataAcquisitionSystem',
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('board_id', sqlmodel.sql.sqltypes.GUID(), nullable=True),
    sa.Column('transmitter_id', sqlmodel.sql.sqltypes.GUID(), nullable=True),
    sa.Column('sensor_id', sqlmodel.sql.sqltypes.GUID(), nullable=True),
    sa.Column('id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['board_id'], ['Board.id'], ),
    sa.ForeignKeyConstraint(['sensor_id'], ['Sensor.id'], ),
    sa.ForeignKeyConstraint(['transmitter_id'], ['Transmitter.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_DataAcquisitionSystem_id'), 'DataAcquisitionSystem', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_DataAcquisitionSystem_id'), table_name='DataAcquisitionSystem')
    op.drop_table('DataAcquisitionSystem')
    op.drop_index(op.f('ix_Sensor_id'), table_name='Sensor')
    op.drop_table('Sensor')
    op.drop_index(op.f('ix_Transmitter_id'), table_name='Transmitter')
    op.drop_table('Transmitter')
    op.drop_index(op.f('ix_MeasurementType_id'), table_name='MeasurementType')
    op.drop_table('MeasurementType')
    op.drop_index(op.f('ix_Board_id'), table_name='Board')
    op.drop_table('Board')
    # ### end Alembic commands ###
