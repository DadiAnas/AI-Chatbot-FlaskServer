import mysql.connector as mysql

def connect_to_database():
    host = "remotemysql.com"
    user = "BMxspwB2gu"
    password = "5tsE1A5jRB"  # settings.MYSQL_DATABASE_PASSWORD
    database = 'BMxspwB2gu'

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
