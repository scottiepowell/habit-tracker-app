# config.py
import os

class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY')
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '../instance', 'site.db')
    SESSION_TYPE = 'filesystem'

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'