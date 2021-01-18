from flask import Blueprint, request, jsonify
import json
from project.config import session_factory #, BrokerConfig
from project.deepLearning.train_chatbot import train_chatbot
from project.deepLearning.chatbot import chatbot_response, get_data_from_db
from project.model import tag_model, context_model
from project.model import response_model
from project.model import pattern_model
# from celery import Celery
#
# broker_url = 'amqp://test:test@localhost:5672//'          # Broker URL for RabbitMQ task queue

chat_bot = Blueprint('chat_bot', __name__)

# celery = Celery(chat_bot.name, broker=broker_url)
# celery.config_from_object(BrockerConfig)


# @celery.task(bind=True)
@chat_bot.route('/message', methods=['GET', 'POST'])
def respond():
    # Retrieve the name from url parameter
    if request.method == 'GET':
        message = str(request.args.get("message", str)).encode('utf8').decode('utf8')
    else:
        message = str(request.json.get("message", str)).encode('utf8').decode('utf8')
        print(message)
    chatbot_rep = chatbot_response(message)

    # For debugging
    print(f"got message {message}")
    print(f"response: {chatbot_rep}")
    response = {
        'id': '0',
        'trigger': '1',
    }

    # Check if user sent a message at all
    if not message:
        response["ERROR"] = "no message found, please send a message."
    # Now the user entered a valid message
    else:
        response["message"] = f"{chatbot_rep}"

    # Return the response in json format
    return jsonify(response)




@chat_bot.route('/train')
async def train_chatbot_model():
    print("[INFO] Chatbot model is training...")
    if await train_chatbot(get_data_from_db()):
        return jsonify({'response': 'chatbot well trained'})
    else:
        return jsonify({'error': 'chatbot wasn\'t trained well'})


def convertJsonFile(file_name, convert=False):
    with open('datasets/' + file_name, encoding='utf-8') as json_file:
        data = json.load(json_file)
        intents = data['intents']
    if convert is False:
        return intents
    else:
        tag = {'tag': '', 'patterns': [], 'responses': [], 'contexts': []}
        tags = []
        for intent in intents:
            tag['tag'] = intent['intent']
            for value in intent['examples']:
                tag['patterns'].append(value)
            tags.append(tag)
            tag = {'tag': '', 'patterns': [], 'responses': [], 'contexts': []}

        entities = data['entities']
        tag = {'tag': '', 'patterns': [], 'responses': [], 'contexts': []}
        for entity in entities:
            tag['tag'] = entity['entity']
            for value in entity['values']:
                tag['patterns'].append(value['value'])
            tags.append(tag)
            tag = {'tag': '', 'patterns': [], 'responses': [], 'contexts': []}
        return tags




@chat_bot.route('/jsontodb/<string:filename>')
def insert_tags(filename):
    data = convertJsonFile(file_name=filename + '.json', convert=False)
    new_session = session_factory()
    try:
        for item in data:
            tag = tag_model.Tag(tag=item['tag'])
            new_session.add(tag)
            new_session.flush()
            new_session.refresh(tag)
            id = tag.id_tag
            for pattern in item['patterns']:
                new_session.add(pattern_model.Pattern(pattern=u'%s' % pattern['text'], tag_id=id))
            for response in item['responses']:
                new_session.add(response_model.Response(response=u'%s' % response['text'], tag_id=id))
        new_session.commit()
        new_session.close()
        return jsonify({"response & patterns": "Successfully added"})
    except:
        new_session.rollback()
        raise


@chat_bot.route('/tag')
def get_tagg():
    return jsonify(get_data_from_db())
