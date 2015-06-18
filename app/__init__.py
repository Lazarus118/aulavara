from flask import Flask
#SQLAlchemy import
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.mail import Mail
from flask.ext.mail import Message

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

lm = LoginManager()
lm.session_protection = "strong"
lm.setup_app(app)

mail = Mail(app)



from app import views, models
