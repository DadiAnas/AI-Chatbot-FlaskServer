from flask import Blueprint,jsonify,request
from .deepLearning.chatbot import chatbot_response

main = Blueprint('main',__name__)

@main.route('/')
def chatbot_home():
    return "ok"

@main.route('/message/', methods=['GET'])
def respond():
    # Retrieve the name from url parameter
    message = str(request.args.get("message", str))
    chatbot_rep = chatbot_response(message)

    # For debugging
    print(f"got message {message}")
    print(f"chatbot response: {chatbot_rep}")

    response = {}

    # Check if user sent a name at all
    if not message:
        response["ERROR"] = "no name found, please send a name."
    # Check if the user entered a number not a name
    elif str(message).isdigit():
        response["ERROR"] = "name can't be numeric."
    # Now the user entered a valid name
    else:
        response["MESSAGE"] = f"{message}"
        response["MESSAGE"] = f"{chatbot_rep}"

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

