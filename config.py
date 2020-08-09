class Config:
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:qazwsxedc@localhost/rest_api'
    SECRET_KEY = 'rkjqeof[ksergpcw.rgcpxz[;e[23[09r,c-58wpoiqw.'


class DevConfig(Config):
    DEBUG = True