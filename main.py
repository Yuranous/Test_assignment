import uvicorn

from src.app import app
from src.settings import HOST, PORT

if __name__ == "__main__":
    uvicorn.run(app, host=HOST, port=PORT)