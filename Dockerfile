FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code/
COPY . /code/
RUN pip install -r requirements.txt
CMD python src/manage.py runserver 0.0.0.0:$PORT