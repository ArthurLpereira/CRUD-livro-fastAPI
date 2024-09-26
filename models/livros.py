from peewee import CharField, AutoField,FloatField ,Model
from config.database import database

class livrosDB(Model):
    id = AutoField()
    nome = CharField()
    genero = CharField()
    num_paginas = CharField()
    autor = CharField()
    editora = CharField()
    preco = FloatField()

    class Meta:
        database = database