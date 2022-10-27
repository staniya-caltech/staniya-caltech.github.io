FROM postgres:15.0
FROM ubuntu:16.04

RUN apt-get update
RUN apt-get -y install python-pip
RUN apt-get update
RUN pip install --upgrade pip
RUN pip install psycopg2-binary

# Set the timezone
ENV TZ=America/Los_Angeles
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
 && echo $TZ > /etc/timezone \
 && dpkg-reconfigure -f noninteractive tzdata

# Custom initialization scripts
COPY ./postgres/create_user.sh   /docker-entrypoint-initdb.d/10-create_user.sh
COPY ./postgres/create_db.sh     /docker-entrypoint-initdb.d/20-create_db.sh
COPY ./postgres/create_extensions.sh     /docker-entrypoint-initdb.d/30-create_extensions.sh

RUN chmod +x /docker-entrypoint-initdb.d/10-create_user.sh \
 && chmod +x /docker-entrypoint-initdb.d/20-create_db.sh \
 && chmod +x /docker-entrypoint-initdb.d/30-create_extensions.sh

COPY ./local_tests.py ./local_tests.py
CMD ["python", "local_tests.py"]