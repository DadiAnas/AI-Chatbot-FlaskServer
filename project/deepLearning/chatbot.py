import nltk
from nltk.stem import WordNetLemmatizer
import pickle
import numpy as np
from keras.models import load_model
import json
import random
from os import getcwd
from tensorflow.compat.v1 import ConfigProto,Session
from keras import backend


config = ConfigProto(
device_count={'GPU': 2},
intra_op_parallelism_threads=1,
allow_soft_placement=True
)

config.gpu_options.allow_growth = True
config.gpu_options.per_process_gpu_memory_fraction = 0.6

session = Session(config=config)
backend.set_session(session)

current_directory = "\\project\\deepLearning\\"
print(current_directory)
lemmatizer = WordNetLemmatizer()
model = load_model(current_directory+'models\\chatbot_model.h5')
intents = json.loads(open(current_directory+'data\\intents.json').read())
words = pickle.load(open(current_directory+'pickles\\words.pkl', 'rb'))
classes = pickle.load(open(current_directory+'pickles\\classes.pkl', 'rb'))


def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
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
    return np.array(bag)


def predict_class(sentence, model):
    # filter out predictions below a threshold
    p = bow(sentence, words, show_details=False)
    res = model.predict(np.array([p]))[0]
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
            result = random.choice(i['responses'])
            break
    return result


def chatbot_response(msg):
    try:
        with session.as_default():
            with session.graph.as_default():
                ints = predict_class(msg, model)
                res = getResponse(ints, intents)
                return res
    except:
        print("Error predecting")

print(chatbot_response("hello"))
