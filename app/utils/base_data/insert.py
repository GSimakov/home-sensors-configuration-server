from random import random
import random

from app import crud
from .data import *
from app import crud


async def insert():

    for sensor_type in sensor_types:
        await crud.sensor_type.get()
        await crud.sensor_type.create(obj_in=sensor_type)

    for measurements_type in measurements_types:
        await crud.measurement_type.create(obj_in=measurements_type)

    for transmitter in transmitters:
        await crud.transmitter.create(obj_in=transmitter)
