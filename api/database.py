import psycopg2

connection = psycopg2.connect(
    host='localhost',
    database='postgres',
    user='postgres',
    password='login-password',
    port='5433'
)


def get_all_users():
    cursor = connection.cursor()
    cursor.execute('select id, name from users')
    rows = cursor.fetchall()

    for row in rows:
        print(f'id: {row[0]}, name: {row[1]}')
    cursor.close()
    connection.close()


get_all_users()
