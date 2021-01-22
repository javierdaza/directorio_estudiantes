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
    database = PostgresqlDatabase(config('PEEWEE_DATABASE_URI'))
else:
    database = SqliteDatabase(config('PEEWEE_DATABASE_URI'))


database_proxy.initialize(database)
