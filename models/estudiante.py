import datetime

from peewee import *


db = SqliteDatabase('app.db')


class BaseModel(Model):
    class Meta:
        database = db


class Estudiante(BaseModel):
    nombre_usuario = CharField(max_length=255, unique=True)
    puntaje = IntegerField(default=0)
    fecha_creacion = DateTimeField(default=datetime.datetime.now)
    numero_telefono = CharField(max_length=255)
    email = CharField(max_length=255)
    foto = CharField(max_length=255)
    motivacion = TextField()
