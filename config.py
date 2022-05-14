import os
class Config:

    SECRET_KEY = 'slihbvsdvhjbhnhlmjknhjbgy'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    
    
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    
    
class TestConfig(Config):
    pass
    
    
class ProdConfig(Config):
    # uri = os.getenv('DATABASE_URL')
    uri = "postgres://asuitrwkomcmtb:9f47b5f5960243ce9522e757d1fa5e66fc8cf091692f09ce67d839e24cbe5672@ec2-52-4-104-184.compute-1.amazonaws.com:5432/d1e1gm62ugig86"
    if uri and uri.startswith('postgres://'):
        uri = uri.replace('postgres://', 'postgresql://', 1)
    SQLALCHEMY_DATABASE_URI = uri

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:nancy1234@localhost/pitches'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}