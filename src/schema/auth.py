""" User Authentication """
# pylint: disable=invalid-name
# pylint: disable=missing-docstring
# pylint: disable=unused-argument
# pylint: disable=too-few-public-methods
# pylint: disable=redefined-builtin
import graphene
from graphene import relay
from werkzeug.security import check_password_hash
from ..database.models.barbers import Barber as Barber_Model
from ..utils.messages import Unauthorized
from ..validation.auth_validator import validate_email
from .barber import Barber

class VerifyBarberMutation(relay.ClientIDMutation):
    barber = graphene.Field(Barber)

    class Input:
        email = graphene.String()
        password = graphene.String()

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        email = input.get('email')
        password = input.get('password')

        email_arr = validate_email(email)

        if not email_arr[0]:
            raise Exception(email_arr[1])

        barber = Barber_Model.query.get(email)

        if not check_password_hash(barber.password, password):
            raise Exception(Unauthorized)

        return VerifyBarberMutation(barber=barber)


class AuthMutation(graphene.ObjectType):
    auth = VerifyBarberMutation.Field()
