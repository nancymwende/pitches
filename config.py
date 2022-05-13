import os
class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:nancy1234@localhost/pitches'
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
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL')
    if SQLALCHEMY_DATABASE_URI and SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)
    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}