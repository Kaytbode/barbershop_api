""" ALL GraphlQL schema module """
# pylint: disable=invalid-name
# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
import graphene
from .barber import BarberQuery, BarberMutation

class Query(BarberQuery, graphene.ObjectType):
    pass

class Mutation(BarberMutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
