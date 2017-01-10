FROM python:3.5

COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt