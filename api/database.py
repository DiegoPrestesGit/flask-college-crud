import psycopg2


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
