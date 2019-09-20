""" file through which app is served from """
import os

from pathlib import Path
from dotenv import load_dotenv
from flask import Flask

ENV_PATH = Path('.') / '.env'
load_dotenv(dotenv_path=ENV_PATH)

API_APP = Flask(__name__)
API_APP.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
API_APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
