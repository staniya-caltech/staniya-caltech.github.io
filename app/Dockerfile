# pull official base image
FROM python:3.11.1-alpine

# create the app user
RUN addgroup -S app && adduser -S app -G app

# create directory for the app user
RUN mkdir -p /home/app

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev gcc python3-dev musl-dev \
    && apk del build-deps \
    && apk --no-cache add musl-dev linux-headers g++

# create and activate virtual environment
# using final folder name to avoid path issues with packages
RUN python3 -m venv $HOME/venv
ENV PATH="$HOME/venv/bin:$PATH"

# install dependencies
RUN pip3 install --upgrade pip
COPY ./requirements.txt .
RUN pip3 wheel --no-cache-dir --no-deps --wheel-dir $HOME/wheels -r requirements.txt
RUN pip3 install --no-cache $HOME/wheels/*

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' $APP_HOME/entrypoint.sh
RUN chmod +x $APP_HOME/entrypoint.sh

# copy project
COPY . $APP_HOME

# activate virtual environment
ENV VIRTUAL_ENV=$APP_HOME/venv

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]