# Image official Python 3.7
FROM python:3.8
# WORK DIRECTORY
WORKDIR /usr/src/app_flask_graphql_init

# Copy the requirements as we can note
COPY ./requirements.txt /usr/src/app_flask_graphql_init/requirements.txt

RUN pip3 install -r requirements.txt

COPY . /usr/src/app_flask_graphql_init
EXPOSE 5000

CMD ["python", "manage.py", "runserver"]
