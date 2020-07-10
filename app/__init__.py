from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DevConf


app = Flask(__name__)
app.config.from_object(DevConf)

db = SQLAlchemy(app)

from app.owners.views import owners
app.register_blueprint(owners, url_prefix='/owners')

from app import views