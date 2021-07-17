import os

from dotenv import load_dotenv

load_dotenv()

DEFAULT_FILE_PATH = './signatures.tsv'
DEFAULT_FILE_SEPARATOR = '\t'

FILE_PATH = os.environ.get('FILE_PATH', '')
if not FILE_PATH:
    FILE_PATH = DEFAULT_FILE_PATH

FILE_SEPARATOR = os.environ.get('FILE_SEPARATOR', '')
if not FILE_SEPARATOR:
    FILE_SEPARATOR = DEFAULT_FILE_SEPARATOR
