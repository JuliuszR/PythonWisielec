from peewee import *
from playhouse.shortcuts import model_to_dict
import hashlib

baza = SqliteDatabase('test.db')

class BazaModel(Model):
    class Meta:
        database = baza

class User(BazaModel):
    login = TextField(unique=True, null=False)
    password = TextField(null=False)

baza.connect()

def hash_password(password):
    return hashlib.sha512(password.encode('utf-8')).hexdigest()

def register(login, password):
    if User.select().where(User.login==login).exists():
        return False, "Uzytkownik juz istnieje"
    User.create(login=login, password=hash_password(password))
    return True, "Zarejestrowano uzytkownika"

def login(login, password):
    hashed = hash_password(password)
    try:
        user = User.get((User.login==login) & (User.password==hashed))
        return True, model_to_dict(user)
    except User.DoesNotExist:
        return False, "Bledny login lub haslo"