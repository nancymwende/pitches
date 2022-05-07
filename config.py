import os
class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:nancy1234@localhost/pitches'

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL')

class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}