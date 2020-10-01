from flask import Blueprint,jsonify
from . import db,cursor

main = Blueprint('main',__name__)


@main.route('/')
def hello_world():
    #query = "CREATE TABLE intents (id INT NOT NULL PRIMARY KEY, name VARCHAR(40) )"
    #cursor.execute(query)
    #query = "INSERT INTO intents (id,name) VALUES ('{}','{}');".format(2,"anas")
    #cursor.execute(query)
    #query = "ALTER TABLE intents DROP COLUMN Updated_at; "
    #cursor.execute(query)
    #db.commit()
    query="SELECT * FROM intents"
    cursor.execute(query)
    print(cursor.column_names)
    intents = cursor.fetchall()
    response = dict()
    for intent in intents:
        response[intent[0]]=intent[1]
    return jsonify({"response:":response})
