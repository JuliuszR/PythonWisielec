#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from peewee import *

if os.path.exists('test.db'):
    #os.remove('test.db')
    pass

baza = SqliteDatabase('test.db')

class BazaModel(Model):
    class Meta:
        database = baza

class Haslo(BazaModel):
    tekst = TextField(null=False)

class User(BazaModel):
    login = TextField(null=False)
    password = TextField(null=False)

baza.connect()
baza.create_tables([Haslo, User], safe=True)


if Haslo().select().count() == 0:
    inst_haslo = Haslo(tekst="python")
    inst_haslo.save()

inst_haslo = Haslo.select().where(Haslo.tekst == "python").get()

def readData():
    for haslo in Haslo.select():
        print(haslo.tekst)
    print()

readData()