from random import random
import random

from app import crud
from .data import *
from app import crud


async def insert():
    pass
#
#     for sensor in sensors:
#         current_sensor = await crud.sensor.get_by_name(name=sensor.name)
#         if not current_sensor:
#             await crud.sensor.create(obj_in=sensor)
#
#     for sensor_type in sensor_types:
#         current_sensor_type = await crud.sensor_type.get_by_name(name=sensor_type.name)
#         if not current_sensor_type:
#             await crud.sensor_type.create(obj_in=sensor_type)
#
#     for measurements_type in measurements_types:
#         current_measurement_type = await crud.measurement_type.get_by_name(name=measurements_type.name)
#         if not current_measurement_type:
#             await crud.measurement_type.create(obj_in=measurements_type)
#
#     for transmitter in transmitters:
#         current_transmitter = await crud.transmitter.get_by_mac(mac=transmitter.MAC)
#         if not current_transmitter:
#             await crud.transmitter.create(obj_in=transmitter)
#

