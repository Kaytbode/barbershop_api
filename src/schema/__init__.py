""" ALL GraphlQL schema module """
# pylint: disable=invalid-name
# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
import graphene
from .barber import BarberQuery, BarberMutation
from .auth import AuthMutation
from .service import ServiceMutation

class Query(BarberQuery, graphene.ObjectType):
    pass

class Mutation(BarberMutation, AuthMutation, ServiceMutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
