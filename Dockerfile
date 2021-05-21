FROM python:3.7

WORKDIR /app
COPY src /app/
COPY requirements.txt .
RUN pip3 install -r requirements.txt
CMD python3 run.py
