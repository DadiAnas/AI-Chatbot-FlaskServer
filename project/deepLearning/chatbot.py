from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
from pickle import load
from numpy import array
from keras.models import load_model
from json import loads
from random import choice
from tensorflow.compat.v1 import Session
from keras import backend



session = Session()
backend.set_session(session)

current_directory = 'project/deepLearning/'
lemmatizer = WordNetLemmatizer()
modelfile = load_model(current_directory+'chatbot_model.h5')
intents = loads(open(current_directory+'intents.json').read())
words = load(open(current_directory+'words.pkl', 'rb'))
classes = load(open(current_directory+'classes.pkl', 'rb'))


def clean_up_sentence(sentence):
    sentence_words = word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
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
    for i in list_of_intents:
        if (i['tag'] == tag):
            result = choice(i['responses'])
            break
    return result


def chatbot_response(msg):
    try:
        with session.as_default():
            with session.graph.as_default():
                ints = predict_class(msg, modelfile)
                res = getResponse(ints, intents)
                return res
    except:
        print("Error predecting")

print(chatbot_response("hello"))
