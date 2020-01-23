import os


class Config:
    
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://postgres:kent123kk@localhost/pool'
    UPLOADED_PHOTOS_DEST ='app/static/photos'


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True
    SECRET_KEY= 'c8840fc92e6bea3838173d4599e18439'

config_options = {
'development':DevConfig,
'production':ProdConfig
}