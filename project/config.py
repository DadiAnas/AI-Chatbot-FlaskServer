import mysql.connector as mysql

def connect_to_database():
    host = "localhost"
    user = "root"
    password = ""  # settings.MYSQL_DATABASE_PASSWORD
    database = 'chatbot__db'

    config = {
        'user': user,
        'password': password,
        'host': host,
        'database': database,
        'raise_on_warnings': True
    }
    return mysql.connect(**config)


db = connect_to_database()
cursor = db.cursor(buffered=True)
