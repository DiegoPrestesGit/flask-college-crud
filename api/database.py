import psycopg2
import uuid
from datetime import date


def create_connection():
    return psycopg2.connect(
        host='localhost',
        database='postgres',
        user='postgres',
        password='login-password',
        port='5433'
    )


def get_all_users():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('select id, name from users')
    rows = cursor.fetchall()
    users = []

    for row in rows:
        user = (f'id: {row[0]}, name: {row[1]}')
        users.append(user)

    cursor.close()
    connection.close()

    return users


def get_user_by_id(user_id):
    connection = create_connection()
    cursor = connection.cursor()
    user_id_formated = "'{0}'".format(user_id)
    cursor.execute('SELECT id, name, email, password FROM users WHERE id = {0}'.format(
        user_id_formated))
    user_data = cursor.fetchone()
    user_formated = (
        'user: {0}'.format(user_data[0]),
        'name: {0}'.format(user_data[1]),
        'email: {0}'.format(user_data[2]),
        'password: {0}'.format(user_data[3]))

    cursor.close()
    connection.close()

    return user_formated


def create_user(name, email, password):
    connection = create_connection()
    cursor = connection.cursor()
    user_id = uuid.uuid1()
    date_now = date.today()
    name_formated = "'{0}'".format(name)
    email_formated = "'{0}'".format(email)
    password_formated = "'{0}'".format(password)
    date_formated = "'{0}'".format(date_now)
    user_id_formated = "'{0}'".format(user_id)
    cursor.execute(
        '''INSERT INTO users(id, name, email, password, created_at, updated_at)
        VALUES({0}, {1}, {2}, {3}, {4})'''.format(
            user_id_formated, name_formated, email_formated, password_formated, date_formated, date_formated
        ))

    cursor.close()
    connection.close()
