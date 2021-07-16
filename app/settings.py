import os

from dotenv import load_dotenv

load_dotenv()

FILE_PATH = os.environ.get('FILE_PATH', '')
if not FILE_PATH:
    raise ValueError('FILE_PATH environment variable value must be provided')

FILE_SEPARATOR = os.environ.get('FILE_SEPARATOR', '')
if not FILE_SEPARATOR:
    raise ValueError('FILE_SEPARATOR environment variable value must be provided')
