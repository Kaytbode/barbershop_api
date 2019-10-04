""" Database Test configuration """
# pylint: disable=redefined-outer-name
# pylint: disable=too-few-public-methods
import os

class TestConfig():
    """ Database test configuration """
    DEBUG = True
    SECRET_KEY = 'barber_dev_key'
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DB')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = True

