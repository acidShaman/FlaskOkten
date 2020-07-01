from flask import Flask
from config import DevConf

app = Flask(__name__)
app.config.from_object(DevConf)

from app import views





