import os
import click


class Config(object):
    """
    This will be create the part of the Configuration of the app

    """
    ENV = os.environ["ENV"] if "ENV" in os.environ else "DEVELOPMENT"
    CRSF_ENABLED = True
    SECRET_KEY = "some_secret_key"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://" + os.environ["DB_USERNAME"] + ":" \
                              + os.environ["DB_PASSWORD"] + "@" \
                              + os.environ["DB_HOST"] + ":" \
                              + os.environ["DB_PORT"] + "/" \
                              + os.environ["DB_DATABASE"]

    click.echo(SQLALCHEMY_DATABASE_URI)


class TestingConfiguration(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://" + os.environ["DB_USERNAME"] + ":" \
                              + os.environ["DB_PASSWORD"] + "@" \
                              + os.environ["DB_HOST"] + ":" \
                              + os.environ["DB_PORT"] + "/" \
                              + os.environ["DB_DATABASE"]


# Here we can define a structure data to call inside of the manner to call inside of the next manner


