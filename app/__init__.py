from flask import Flask
from config import DevConf
from .clients.views import clients
from .pets.views import pets

app = Flask(__name__)
app.config.from_object(DevConf)
app.register_blueprint(clients, url_prefix='/clients')
app.register_blueprint(pets, url_prefix='/pets')

from app import views