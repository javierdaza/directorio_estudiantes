from urllib.parse import urlparse

import datetime

from decouple import config
from peewee import *


database_proxy = DatabaseProxy()
production = config('PRODUCTION', cast=bool)


class BaseModel(Model):
    class Meta:
        database = database_proxy


class Estudiante(BaseModel):
    nombre_usuario = CharField(max_length=255, unique=True)
    puntaje = IntegerField(default=0)
    fecha_creacion = DateTimeField(default=datetime.datetime.now)
    numero_telefono = CharField(max_length=255)
    email = CharField(max_length=255)
    foto = CharField(max_length=255)
    motivacion = TextField()


if production:
    if config('HEROKU', cast=int) == 1:
        url = urlparse(config('DATABASE_URL'))
        database = PostgresqlDatabase(
            database=url.path[1:],
            user=url.username,
            password=url.password,
            host=url.hostname,
            port=url.port,
            autorollback=True
        )
    else:
        database = SqliteDatabase(config('DATABASE_URL'))
else:
    database = SqliteDatabase(config('DATABASE_URL'))


database_proxy.initialize(database)
