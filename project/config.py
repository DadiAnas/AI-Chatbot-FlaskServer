import mysql.connector as mysql

def db():
    host = "www.db4free.net"
    user = "chatbot__db"
    password = "chatbot__db"  # settings.MYSQL_DATABASE_PASSWORD
    database = 'chatbot__db'

    config = {
        'user': user,
        'password': password,
        'host': host,
        'database': database,
        'raise_on_warnings': True
    }

    return mysql.connect(**config)

db = db()
cursor = db.cursor(buffered=True)


