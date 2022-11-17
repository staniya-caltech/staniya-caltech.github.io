FROM postgres:15.0

FROM python:3.11
ENV CQLENG_ALLOW_SCHEMA_MANAGEMENT="True"
RUN pip install psycopg2-binar

# Set the timezone
ENV TZ=America/Los_Angeles
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
 && echo $TZ > /etc/timezone \
 && dpkg-reconfigure -f noninteractive tzdata

# Custom initialization scripts
COPY ./create_user.sh   /docker-entrypoint-initdb.d/10-create_user.sh
COPY ./create_db.sh     /docker-entrypoint-initdb.d/20-create_db.sh
COPY ./create_extensions.sh     /docker-entrypoint-initdb.d/30-create_extensions.sh

RUN chmod +x /docker-entrypoint-initdb.d/10-create_user.sh \
 && chmod +x /docker-entrypoint-initdb.d/20-create_db.sh \
 && chmod +x /docker-entrypoint-initdb.d/30-create_extensions.sh

