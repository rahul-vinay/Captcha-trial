import uuid
import logging
from flask import Flask, request, render_template
from flask_session import Session
from flask_session_captcha import FlaskSessionCaptcha
from pymongo import MongoClient

app = Flask(__name__)

mongoClient = MongoClient('localhost', 27017)

#captcha config

app.config["SECRET_KEY"] = uuid.uuid4()
app.config['CAPTCHA_ENABLE'] = True

app.config['CAPTCHA_LENGTH'] = 5

app.config['CAPTCHA_WIDTH'] = 160
app.config['CAPTCHA_HEIGHT'] = 60
app.config['SESSION_MONGODB'] = mongoClient
app.config['SESSION_TYPE'] = 'mongodb'
app.config['SESSION_COOKIE_NAME'] = 'your_session_cookie_name'


Session(app) #enable server session

captcha = FlaskSessionCaptcha(app)


@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == "POST":
        if captcha.validate():
            return "success"
        else:
            return "fail"
    return render_template('form.html')

if __name__ == "__main__":
    app.run(debug=True)
    logging.getLogger().setLevel("DEBUG")
    app.run()

