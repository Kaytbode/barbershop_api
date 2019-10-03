''' Authentication test module '''
# pylint: disable=too-few-public-methods
# pylint: disable=redefined-outer-name
# pylint: disable=unused-argument
import os
import pytest

from graphene.test import Client
from ..schema import schema
from .. import build_app
from ..database.models import db as _db

class TestConfig():
    """ Database test configuration """
    DEBUG = True
    SECRET_KEY = 'barber_dev_key'
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DB')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = True


@pytest.fixture(scope='session')
def app():
    """ App configuration and database initialization """
    _app = build_app(TestConfig)
    ctx = _app.app_context()
    ctx.push()

    _db.create_all()

    yield _app

    _db.drop_all()
    ctx.pop()

@pytest.fixture(scope='session')
def testapp(app):
    """ test client for app """
    return app.test_client()


def test_registration(testapp):
    """ Registration test """
    client = Client(schema)
    executed = client.execute(
        '''
        mutation{
            createBarber(input: {
                email:"abced@yahoo.com",
                firstName: "abc",
                lastName: "xyz",
                password: "u9j2ieor",
                confirmPassword: "u9j2ieor"
            }){
                barber{
                    email,
                    firstName,
                    lastName
                }
            }
        }
        '''
    )
    assert executed == {
        "data": {
            "createBarber": {
                "barber": {
                    "email": "abced@yahoo.com",
                    "firstName": "abc",
                    "lastName": "xyz"
                }
            }
        }
    }
