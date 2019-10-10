""" GraphlQL Service schema module """
# pylint: disable=too-few-public-methods
# pylint: disable=missing-docstring
# pylint: disable=unused-argument
# pylint: disable=redefined-builtin
# pylint: disable=no-init
from datetime import datetime
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from ..database.models.services import Service as Service_Model
from ..validation.auth_validator import validate_name, validate_email
from ..utils.location import get_address


class Service(SQLAlchemyObjectType):
    ''' a service '''
    class Meta:
        model = Service_Model
        interfaces = (relay.Node, )

class ServiceConnection(relay.Connection):
    class Meta:
        node = Service

class ServiceQuery(graphene.ObjectType):
    ''' Query service table in database '''
    node = relay.Node.Field()

    service = relay.Node.Field(Service)

    all_services = SQLAlchemyConnectionField(ServiceConnection, sort=None)


# Mutation
class CreateService(relay.ClientIDMutation):
    service = graphene.Field(Service)

    class Input:
        customer = graphene.String()
        barber_email = graphene.String()

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        email_arr = validate_email(input.get('barber_email'))
        customer_name_arr = validate_name(input.get('customer'))

        if not email_arr[0]:
            raise Exception(email_arr[1])

        if not customer_name_arr[0]:
            raise Exception(customer_name_arr[1])

        service = Service_Model(
            customer=input.get('customer'),
            location=get_address(),
            barber=input.get('barber_email'),
            start=datetime.now(),
            status='current'
        )

        service.add_service()

        return CreateService(service=service)


class ServiceMutation(graphene.ObjectType):
    ''' Insert barber into the database '''
    create_service = CreateService.Field()
