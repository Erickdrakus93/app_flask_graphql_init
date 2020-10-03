
from flask_graphql_auth import (
    create_access_token, create_refresh_token
)
from graphene import *


class ExampleQuery(ObjectType):
    test = String()

    @classmethod
    def resolve_test(cls, info):
        return "test ok"


class RootQuery(ExampleQuery, ObjectType):
    pass


class AuthMutation(Mutation):
    class Arguments:
        username = String(required=True)
        password = String(required=True)

    access_token = String()
    refresh_token = String()

    @classmethod
    def mutate(cls, info, username, password):
        """
        This class is to create the mutation in the side of the graphql
        :param info:
        :param username: Graphene.String type
        :param password: Graphene.String type
        :return: JWT token type
        """
        return AuthMutation(
            access_token=create_access_token(username, password),
            refresh_token=create_refresh_token(username),
        )


schema = Schema(query=RootQuery, mutation=None)
