from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_graphql import GraphQLView

db = SQLAlchemy()


# Here we define the next part of the main examples
# Here we define the next part of a factory app pattern

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def test_route():
        return "The test is ok"

    return app


def create_environment_configuration():
    """
    This function is to set the configuration of the app
    :return: Configuration Environment
    """
    if Config.ENV == 'TESTING':
        return "config.TestingConfiguration"
    else:
        return "config.DevelopmentConfig"
