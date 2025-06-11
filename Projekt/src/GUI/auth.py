# auth.py

import hashlib
from peewee import *

baza = SqliteDatabase('test.db')

class BazaModel(Model):
    """
    Klasa bazowa bazy danych
    """
    class Meta:
        database = baza

class User(BazaModel):
    """
    Tabela User w bazie danych z loginem, hasłem i iloscia wygranych
    """
    login = TextField(unique=True, null=False)
    password = TextField(null=False)
    wins = IntegerField(default=0)

baza.connect()
baza.create_tables([User], safe=True)

def hash_password(password):
    """
    :param password:
    :return: hashed password
    """
    return hashlib.sha256(password.encode()).hexdigest()

def register(login_input, password):
    """

    :param login_input: wpisany login
    :param password: wpisane haslo
    :return: nowy record User
    """
    if User.select().where(User.login == login_input).exists():
        return False, "Użytkownik już istnieje"
    User.create(login=login_input, password=hash_password(password), wins=0)
    return True, "Zarejestrowano pomyślnie"

def login(login_input, password):
    """

    :param login_input: wpisany login
    :param password: wpisane haslo
    :return: Loguje
    """
    hashed = hash_password(password)
    try:
        user = User.get((User.login == login_input) & (User.password == hashed))
        return True, user
    except User.DoesNotExist:
        return False, "Błędny login lub hasło"

def add_win_to_user(user_id):
    """
    :param user_id: id uzytkownika
    :return: +1 wygrana
    """
    user = User.get_by_id(user_id)
    user.wins += 1
    user.save()

def get_user_by_login(login_input):
    try:
        return User.get(User.login == login_input)
    except User.DoesNotExist:
        return None