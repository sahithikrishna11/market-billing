FROM python:3.5
WORKDIR /app
EXPOSE 8000
ADD requirements.txt /app/requirements.txt
RUN ["pip", "install", "-r", "requirements.txt"]
ADD . /app
CMD python manage.py runserver