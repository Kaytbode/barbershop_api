""" flask factory module """
import os

from pathlib import Path
from dotenv import load_dotenv
from flask import Flask
from src.database.models import db, migrate

ENV_PATH = Path('.') / '.env'
load_dotenv(dotenv_path=ENV_PATH)

def build_app():
    """ flask factory """
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY') or 'barber_dev_key',
        SQLALCHEMY_DATABASE_URI=os.getenv('DATABASE_URL'),
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )

    db.init_app(app)
    migrate.init_app(app, db)

    @app.route('/')
    def hello(): # pylint: disable=unused-variable
        return 'Hello, World!'

    return app
