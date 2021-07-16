FROM tiangolo/uvicorn-gunicorn:python3.8

LABEL app.version="0.0.1-beta"

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .