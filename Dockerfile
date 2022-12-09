# Pull Official Python base image
FROM python:3.11

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the timezone
ENV TZ=America/Los_Angeles
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
 && echo $TZ > /etc/timezone \
 && dpkg-reconfigure -f noninteractive tzdata

# install dependencies
RUN pip install --upgrade cython
RUN pip install --upgrade pip
COPY ./Pipfile Pipfile.lock /usr/src/app/
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

