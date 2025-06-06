# auth.py

import hashlib
from peewee import *

baza = SqliteDatabase('test.db')

class BazaModel(Model):
    class Meta:
        database = baza

class User(BazaModel):
    login = TextField(unique=True, null=False)
    password = TextField(null=False)
    wins = IntegerField(default=0)

baza.connect()
baza.create_tables([User], safe=True)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register(login_input, password):
    if User.select().where(User.login == login_input).exists():
        return False, "Użytkownik już istnieje"
    User.create(login=login_input, password=hash_password(password), wins=0)
    return True, "Zarejestrowano pomyślnie"

def login(login_input, password):
    hashed = hash_password(password)
    try:
        user = User.get((User.login == login_input) & (User.password == hashed))
        return True, {"id": user.id, "login": user.login, "wins": user.wins}
    except User.DoesNotExist:
        return False, "Błędny login lub hasło"

def add_win_to_user(user_id):
    user = User.get_by_id(user_id)
    user.wins += 1
    user.save()
