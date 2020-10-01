from flask import Blueprint,jsonify,request
from .config import db,cursor

main = Blueprint('main',__name__)


@main.route('/')
def hello_world():
    query="SELECT * FROM intents"
    cursor.execute(query)
    print(cursor.column_names)
    intents = cursor.fetchall()
    response = dict()
    for intent in intents:
        response[intent[0]]=intent[1]
    return jsonify({"response:":response}) or "<h1>Welcome to chatbot server !!</h1>"

@main.route('/getmsg/', methods=['GET'])
def respond():
    # Retrieve the name from url parameter
    name = request.args.get("name", None)

    # For debugging
    print(f"got name {name}")

    response = {}

    # Check if user sent a name at all
    if not name:
        response["ERROR"] = "no name found, please send a name."
    # Check if the user entered a number not a name
    elif str(name).isdigit():
        response["ERROR"] = "name can't be numeric."
    # Now the user entered a valid name
    else:
        response["MESSAGE"] = f"Welcome {name} to our awesome platform!!"

    # Return the response in json format
    return jsonify(response)

@main.route('/post/', methods=['POST'])
def post_something():
    name = request.form.get('name')
    print(name)
    # You can add the test cases you made in the previous function, but in our case here you are just testing the POST functionality
    if name:
        return jsonify({
            "Message": f"Welcome {name} to our awesome platform!!",
            # Add this option to distinct the POST request
            "METHOD" : "POST"
        })
    else:
        return jsonify({
            "ERROR": "no name found, please send a name."
        })

