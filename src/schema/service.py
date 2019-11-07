""" GraphlQL Service schema module """
# pylint: disable=too-few-public-methods
# pylint: disable=missing-docstring
# pylint: disable=unused-argument
# pylint: disable=redefined-builtin
# pylint: disable=no-init
# pylint: disable=no-member
import os

from datetime import datetime
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from ..database.models.services import Service as Service_Model
from ..validation.auth_validator import validate_name, validate_email
from ..validation.service_validator import validate_id
from ..utils.location import get_address
from ..database.models import db


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
        latitude = graphene.String()
        longitude = graphene.String()

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
            location=get_address(input.get('latitude'), input.get('longitude')),
            barber=input.get('barber_email'),
            start=datetime.now(),
            status='current'
        )

        service.add_service()

        return CreateService(service=service)

class UpdateService(relay.ClientIDMutation):
    service = graphene.Field(Service)

    class Input:
        service_id = graphene.String()

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        service_id = input.get('service_id')
        id_arr = validate_id(service_id)

        if not id_arr[0]:
            raise Exception(id_arr[1])

        service = Service_Model.get_service(service_id)

        stop = datetime.now()
        time_difference = stop - service.start
        duration = int(time_difference.total_seconds())

        fee = duration * int((os.getenv('FEE')))

        service.service_id = service_id
        service.stop = stop
        service.duration = duration
        service.fee = '{}'.format(fee)
        service.status = 'done'

        db.session.commit()

        return UpdateService(service=service)

class ServiceMutation(graphene.ObjectType):
    ''' Insert barber into the database '''
    create_service = CreateService.Field()
    update_service = UpdateService.Field()
