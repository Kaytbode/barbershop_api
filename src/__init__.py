""" flask factory module """
# pylint: disable=invalid-name
import os

from pathlib import Path
from dotenv import load_dotenv
from flask import Flask
from flask_graphql import GraphQLView
from src.database.models import db, migrate
from src.schema import schema

ENV_PATH = Path('.') / '.env'
load_dotenv(dotenv_path=ENV_PATH)

def build_app(TestConfig=None):
    """ flask factory """
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY') or 'barber_dev_key',
        SQLALCHEMY_DATABASE_URI=os.getenv('DATABASE_URL'),
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )

    if TestConfig is not None:
        app.config.from_object(TestConfig)

    db.init_app(app)
    migrate.init_app(app, db)

    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view(
            'graphql',
            schema=schema,
            graphiql=True # for having the GraphiQL interface
        )
    )

    return app
