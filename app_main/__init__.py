from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# Here we define the next part of the main examples
# Here we define the next part of a factory app pattern

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def test_route():
        return "The test is ok"

    return app
