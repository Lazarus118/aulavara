from flask import Flask
#SQLAlchemy import
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

lm = LoginManager()
lm.session_protection = "strong"
lm.setup_app(app)

from app import views, models
