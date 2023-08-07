FROM python:3.11-slim

# Allow statements and log messages to immediately appear in the logs
ENV PYTHONUNBUFFERED True

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

#COPY ./requirements.txt /app/requirements.txt

#RUN pip install --upgrade pip

RUN pip --no-cache-dir install -r requirements.txt

COPY . /app

EXPOSE 8080

# CMD ["python", "src/main.py"]

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app