""" GraphlQL Barber schema module """
# pylint: disable=too-few-public-methods
# pylint: disable=missing-docstring
# pylint: disable=unused-argument
# pylint: disable=redefined-builtin
# pylint: disable=no-init
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from werkzeug.security import generate_password_hash
from ..database.models.barbers import Barber as Barber_Model

# Query
class Barber(SQLAlchemyObjectType):
    ''' Just a user, in this case barber '''
    class Meta:
        model = Barber_Model
        interfaces = (relay.Node, )

class BarberConnection(relay.Connection):
    class Meta:
        node = Barber


class BarberQuery(graphene.ObjectType):
    ''' Query barber table in database '''
    node = relay.Node.Field()

    all_barbers = SQLAlchemyConnectionField(BarberConnection, sort=None)


# Mutation
class CreateBarber(relay.ClientIDMutation):
    barber = graphene.Field(Barber)

    class Input:
        email = graphene.String()
        first_name = graphene.String()
        last_name = graphene.String()
        password = graphene.String()

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        barber = Barber_Model(
            email=input.get('email'),
            first_name=input.get('first_name'),
            last_name=input.get('last_name'),
            password=generate_password_hash(input.get('password')),
        )

        barber.save_barber()

        return CreateBarber(barber=barber)

class BarberMutation(graphene.AbstractType):
    ''' Insert barber into the database '''
    create_barber = CreateBarber.Field()