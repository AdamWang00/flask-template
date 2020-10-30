from os import environ

class Config:
    DEBUG = environ["DEBUG"].lower() == "true" if "DEBUG" in environ else False
    
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = environ['EMAIL_USER']
    MAIL_PASSWORD = environ['EMAIL_PASS']
    MAIL_TO = environ['EMAIL_TO']

    SECRET_KEY = environ['SECRET_KEY']
    REGISTRATION_KEY = environ['REGISTRATION_KEY']