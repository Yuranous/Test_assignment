import os

from dotenv import load_dotenv

load_dotenv()

PORT = int(os.environ.get('PORT', 8000))
HOST = os.environ.get('HOST', '0.0.0.0')
FILE_PATH = os.environ.get('FILE_PATH', '')
