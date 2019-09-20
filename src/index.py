""" file through which app is served from """
import os

from pathlib import Path
from dotenv import load_dotenv

ENV_PATH = Path('.') / '.env'
load_dotenv(dotenv_path=ENV_PATH)

print(os.getenv('PORT'))
