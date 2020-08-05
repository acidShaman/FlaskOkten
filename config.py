class Config:
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:qazwsxedc@localhost/rest_api'


class DevConfig(Config):
    DEBUG = True