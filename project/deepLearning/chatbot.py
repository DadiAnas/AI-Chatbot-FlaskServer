from pickle import load
from numpy import array
from keras.models import load_model
from random import choice
from tensorflow.compat.v1 import Session
from keras import backend

from project.config import get_objects, session_factory
from project.model import tag_model, pattern_model, response_model, context_model

session = Session()
backend.set_session(session)



def get_data_from_db():
    # fetch tags
    fetched = get_objects(tag_model.Tag)

    forma = {"tag": "", "patterns": [], "responses": [], "context": []}
    result = {'intents': []}
    for item in fetched:
        forma['tag'] = str(item.tag).encode("utf8").decode("utf8")
        # fetch patterns
        new_session = session_factory()
        patterns = new_session.query(pattern_model.Pattern).filter_by(tag_id=item.id_tag).all()
        # add patterns to intents
        for pattern in patterns:
            forma['patterns'].append( str(pattern.pattern).encode("utf8").decode("utf8"))

        # fetch responses
        responses = new_session.query(response_model.Response ).filter_by(tag_id=item.id_tag).all()
        # add responses to intents
        for response in responses:
            forma['responses'].append( str(response.response).encode("utf8").decode("utf8"))

        # fetch contexts
        contexts = new_session.query(context_model.Context).filter_by(tag_id=item.id_tag).all()
        # add responses to intents
        for context in contexts:
            forma['context'].append(context.concext)
        print(forma)

        result['intents'].append(forma)
        forma = {"tag": "", "patterns": [], "responses": [], "context": []}
    return result

current_directory = 'project/deepLearning/'
modelfile = load_model(current_directory + 'model/chatbot_model.h5')
intents = get_data_from_db()#loads(open(current_directory + 'intents.json').read())
words = load(open(current_directory + 'pkl/words.pkl', 'rb'))
classes = load(open(current_directory + 'pkl/classes.pkl', 'rb'))


def clean_up_sentence(sentence):
    sentence_words = sentence
    sentence_words = [word.lower() for word in sentence_words]
    return sentence_words


# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence

def bow(sentence, words, show_details=True):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words - matrix of N words, vocabulary matrix
    bag = [0] * len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                # assign 1 if current word is in the vocabulary position
                bag[i] = 1
                if show_details:
                    print("found in bag: %s" % w)
    return array(bag)


def predict_class(sentence, model):
    # filter out predictions below a threshold
    p = bow(sentence, words, show_details=False)
    res = model.predict(array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list


def getResponse(ints, intents_json):
    result = ''
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in  list_of_intents:
        if (i['tag'] == tag):
            result = choice(i['responses'])
            if result is not None:
                break
    return result


def chatbot_response(msg):
    try:

        with session.as_default():
            with session.graph.as_default():
                ints = predict_class(msg, modelfile)
                res = getResponse(ints, intents)
                return res or choice(["Sorry, I can't understand you","Can you repeat on other words"])
    except:
        print("Error predecting")


print(chatbot_response("hello"))
