from random import random
import random

from app import crud
from app import schemas


async def insert():
    measurements_types: list[schemas.IMeasurementTypeCreate] = [
        schemas.IMeasurementTypeCreate(name='Градус Цельсия', unit='°С'),
        schemas.IMeasurementTypeCreate(name='Люмен', unit='лм'),
        schemas.IMeasurementTypeCreate(name='Относительная влажность', unit='%'),
    ]

    for type in measurements_types:
        created_type = await crud.measurement_type.create(obj_in=type)

        sensor: schemas.ISensorCreate = schemas.ISensorCreate(
            name='Датчик{}'.format(random.randint(1, 10000)),
            type='ТипДатчика1',
            measurement_type_id=created_type.id
        )

        board: schemas.IBoardCreate = schemas.IBoardCreate(
            address='192.168.0.10',
            hardware_id='Холодильник{}'.format(random.randint(1,10000)),
            name='BoardFridge{}'.format(random.randint(1, 10000)))

        config: schemas.IConfigCreate = schemas.IConfigCreate(
            name='Конфигурация{}'.format(random.randint(1, 10000)),
            ssid='WIFI',
            password='123',
            conf_url='URLPLACEHOLDER',
            data_url='URLPLACEHOLDER',
            delay=10000
        )


        created_sensor = await crud.sensor.create(obj_in=sensor)
        created_board = await crud.board.create(obj_in=board)
        created_config = await crud.config.create(obj_in=config)

        das: schemas.IDASCreate = schemas.IDASCreate(
            name='СистемаСбора{}'.format(random.randint(1, 10000)),
            board_id=created_board.id,
            sensor_id=created_sensor.id,
            config_id=created_config.id,
            state=False
        )

        await crud.das.create(obj_in=das)
