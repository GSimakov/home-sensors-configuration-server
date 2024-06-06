"""init

Revision ID: 542f93093e83
Revises: 
Create Date: 2024-06-06 15:36:42.083688

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel
import sqlalchemy_utils

# revision identifiers, used by Alembic.
revision: str = '542f93093e83'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Board',
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('description', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('address', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('hardware_id', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_Board_id'), 'Board', ['id'], unique=False)
    op.create_table('Config',
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('ssid', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('password', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('conf_url', sqlalchemy_utils.types.url.URLType(), nullable=True),
    sa.Column('data_url', sqlalchemy_utils.types.url.URLType(), nullable=True),
    sa.Column('delay', sa.Integer(), nullable=False),
    sa.Column('id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_Config_id'), 'Config', ['id'], unique=False)
    op.create_table('MeasurementType',
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('unit', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_MeasurementType_id'), 'MeasurementType', ['id'], unique=False)
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
    sa.Column('sensor_id', sqlmodel.sql.sqltypes.GUID(), nullable=True),
    sa.Column('config_id', sqlmodel.sql.sqltypes.GUID(), nullable=True),
    sa.Column('state', sa.Boolean(), nullable=False),
    sa.Column('id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['board_id'], ['Board.id'], ),
    sa.ForeignKeyConstraint(['config_id'], ['Config.id'], ),
    sa.ForeignKeyConstraint(['sensor_id'], ['Sensor.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_DataAcquisitionSystem_id'), 'DataAcquisitionSystem', ['id'], unique=False)
    op.create_table('JournalDAS',
    sa.Column('DAS_id', sqlmodel.sql.sqltypes.GUID(), nullable=True),
    sa.Column('event', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('status', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['DAS_id'], ['DataAcquisitionSystem.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_JournalDAS_id'), 'JournalDAS', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_JournalDAS_id'), table_name='JournalDAS')
    op.drop_table('JournalDAS')
    op.drop_index(op.f('ix_DataAcquisitionSystem_id'), table_name='DataAcquisitionSystem')
    op.drop_table('DataAcquisitionSystem')
    op.drop_index(op.f('ix_Sensor_id'), table_name='Sensor')
    op.drop_table('Sensor')
    op.drop_index(op.f('ix_MeasurementType_id'), table_name='MeasurementType')
    op.drop_table('MeasurementType')
    op.drop_index(op.f('ix_Config_id'), table_name='Config')
    op.drop_table('Config')
    op.drop_index(op.f('ix_Board_id'), table_name='Board')
    op.drop_table('Board')
    # ### end Alembic commands ###
