# using Python official base image
FROM python:3.10-slim

# Python Interpreter Flags
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Compiler and OS libraries
RUN apt-get update \
  && apt-get install -y --no-install-recommends build-essential libpq-dev \
  && rm -rf /var/lib/apt/lists/*

# project libraries and User Creation
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt \
    && rm -rf /tmp/requirements.txt \
    && useradd -U app_user \
    && install -d -m 0755 -o app_user -g app_user /app/static

# set work directory
WORKDIR /app

# change to the app user
USER app_user:app_user

# chown all the files to the app user
COPY --chown=app_user:app_user . .

#  Docker Run Checks and Configurations
ENTRYPOINT [ "./app/docker/entrypoint.sh" ]
CMD [ "./app/docker/start.sh", "server" ]