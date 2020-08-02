from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from config import DevConf


app = Flask(__name__)
app.config.from_object(DevConf)

db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

from app.owners.views import owners
app.register_blueprint(owners, url_prefix='/owners')

from app.admin import admin
from app import views