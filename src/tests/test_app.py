''' Registeration test module '''
# pylint: disable=redefined-outer-name
# pylint: disable=unused-import
# pylint: disable=unused-argument
import pytest

from graphene.test import Client
from .. import build_app
from ..database.models import db as _db
from ..schema import schema
from . import TestConfig

@pytest.fixture(scope='session')
def app():
    """ App configuration and database initialization """
    _app = build_app(TestConfig)
    ctx = _app.app_context()
    ctx.push()

    _db.drop_all()
    _db.create_all() 

    yield _app

    ctx.pop()

@pytest.fixture(scope='session')
def testapp(app):
    """ test client for app """
    return app.test_client()


def test_registration(testapp):
    """ Successful Registration test """
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

def test_login(testapp):
    """ Successful login test """
    client = Client(schema)
    executed = client.execute(
        '''
        mutation{
            verifyBarber(input: {
                email:"abced@yahoo.com",
                password: "u9j2ieor"
            }){
                barber{
                    email,
                    firstName,
                    lastName,
                }
            }
        }
        '''
    )
    assert executed == {
        "data": {
            "verifyBarber": {
                "barber": {
                    "email": "abced@yahoo.com",
                    "firstName": "abc",
                    "lastName": "xyz"
                }
            }
        }
    }

def test_add_service(testapp):
    """ Successfully add service to the database"""
    client = Client(schema)
    executed = client.execute(
        '''
        mutation{
            createService(input: {
                barberEmail:"abced@yahoo.com",
                customer: "flip burger"
            }){
                service{
                    customer,
                    status
                }
            }
        }
        '''
    )
    assert executed == {
        "data": {
            "createService": {
                "service": {
                    "customer": "flip burger",
                    "status": "current"
                }
            }
        }
    }

def test_update_service(testapp):
    """ Successfully update service in the database"""
    client = Client(schema)
    executed = client.execute(
        '''
        mutation{
            updateService(input: {
                serviceId:"1",
            }){
                service{
                    customer,
                    status,
                    serviceId
                }
            }
        }
        '''
    )
    assert executed == {
        "data": {
            "updateService": {
                "service": {
                    "customer": "flip burger",
                    "status": "done",
                    "serviceId": "1",
                }
            }
        }
    }
