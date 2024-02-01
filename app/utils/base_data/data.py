from app.schemas import ISensorTypeCreate, IMeasurementTypeCreate, ITransmitterCreate, ISensorCreate

sensors: list[ISensorCreate] = [
    ISensorCreate(name='Датчик1', description='описание датчика 1'),
    ISensorCreate(name='Датчик2', description='описание датчика 2'),
    ISensorCreate(name='Датчик3', description='описание датчика 3'),
]

sensor_types: list[ISensorTypeCreate] = [
    ISensorTypeCreate(name="Датчик яркости"),
    ISensorTypeCreate(name="Датчик влажности"),
    ISensorTypeCreate(name="Датчик температуры"),
]

measurements_types: list[IMeasurementTypeCreate] = [
    IMeasurementTypeCreate(name='Градус Цельсия', unit='°С'),
    IMeasurementTypeCreate(name='Люмен', unit='лм'),
    IMeasurementTypeCreate(name='Относительная влажность', unit='%'),
]

transmitters: list[ITransmitterCreate] = [
    ITransmitterCreate(IP='192.168.0.10', MAC='3a:43:cf:fe:7f:4d'),
    ITransmitterCreate(IP='192.168.0.11', MAC='3a:a1:23:e4:56:ce'),
    ITransmitterCreate(IP='192.168.0.12', MAC='3a:56:f7:a4:cd:34'),
]