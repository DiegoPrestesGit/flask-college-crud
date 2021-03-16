import psycopg2
import uuid


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
    cursor.execute('''SELECT * FROM users WHERE id = {0}'''.format(user_id))
    user = cursor.fetchall()

    cursor.close()
    connection.close()

    return user


def create_user(name, email, password):
    connection = create_connection()
    cursor = connection.cursor()
    user_id = uuid.uuid1()
    cursor.execute(
        '''INSERT INTO users(id, name, password)
        VALUES({0}, {1}, {2})'''.format(user_id, name, email, password))

    cursor.close()
    connection.close()
