from flask import Blueprint, request, jsonify
from .deepLearning.chatbot import chatbot_response

chatbot = Blueprint('chatbot', __name__)


@chatbot.route('/message', methods=['GET'])
def respond():
    # Retrieve the name from url parameter
    message = str(request.args.get("message", str))
    chatbot_rep = chatbot_response(message)

    # For debugging
    print(f"got message {message}")
    print(f"response: {chatbot_rep}")
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
