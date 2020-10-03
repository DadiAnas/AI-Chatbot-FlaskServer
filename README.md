# Python: AI-CHATBOT-SERVER

An AI chatbot server, which easily deployed to Heroku.


## Running Locally

Make sure you have Python 3.8 [installed locally](http://install.python-guide.org). To push to Heroku, you'll need to install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).

```sh
$ git clone https://github.com/DadiAnas/AI-Chatbot-FlaskServer.git
$ cd ai-chatbot-flaskserver

$ py -m venv ai-chatbot-flaskserver
$ py -m pip install -r requirements.txt

$ heroku local
```

Your app should now be running on [localhost:5000](http://localhost:5000/). 
It should works just like our deployed version: [Chatbot Server on heroku](https://ai-chatbot-server.herokuapp.com/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku main

$ heroku run python app.py
$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)
