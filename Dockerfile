FROM python:3.9.17-alpine3.18

WORKDIR /app

COPY requirements.txt /app

RUN pip --no-cache-dir install -r requirements.txt

COPY . /app

EXPOSE 4000

CMD ["python", "src/app.py"]