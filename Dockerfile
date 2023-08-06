FROM python:3.9-slim-bullseye

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --upgrade pip

RUN pip --no-cache-dir install -r requirements.txt

COPY . /app

EXPOSE 4000

CMD ["python", "src/app.py"]