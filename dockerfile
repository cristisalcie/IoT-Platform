FROM python:3.6

COPY requirements.txt /tmp
RUN pip install -U setuptools
RUN pip install -r /tmp/requirements.txt
COPY /src /app
WORKDIR /app
EXPOSE 8080
# CMD ["python3", "mqtt_adapter.py"]
