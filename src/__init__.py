""" file through which app is served from """
import os

from pathlib import Path
from dotenv import load_dotenv
from flask import Flask

ENV_PATH = Path('.') / '.env'
load_dotenv(dotenv_path=ENV_PATH)

app = Flask(__name__) # pylint: disable=invalid-name
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route('/')
def hello():
    """ hello world test server """
    return 'Hello, World!'
