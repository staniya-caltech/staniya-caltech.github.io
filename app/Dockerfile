###########
# BUILDER #
###########

# using ubuntu LTS version
FROM ubuntu:20.04 AS builder-image

# set work directory
WORKDIR /usr/src/app

# avoid stuck build due to user prompt
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install --no-install-recommends -y python3.9 python3.9-dev python3-pip python3-wheel build-essential && \
    apt install -y netcat && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# install requirements
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt

#########
# FINAL #
#########

FROM ubuntu:20.04 AS runner-image

# create directory for the app user
RUN mkdir -p /home/app

# create the app user
RUN addgroup --system app && adduser --system --group app

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# install dependencies
RUN apt-get update && apt-get install --no-install-recommends -y python3.9 python3-pip && \
    apt install -y netcat && \
    apt-get clean && rm -rf /var/lib/apt/list
COPY --from=builder-image /usr/src/app/wheels /wheels
COPY --from=builder-image /usr/src/app/requirements.txt .
RUN pip install --no-cache /wheels/*

# copy entrypoint.prod.sh
COPY ./entrypoint.prod.sh .
RUN sed -i 's/\r$//g'  $APP_HOME/entrypoint.prod.sh
RUN chmod +x  $APP_HOME/entrypoint.prod.sh

# copy project
COPY . $APP_HOME

# make sure all messages always reach console
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

# chown all the files to the app user
RUN chown -R app:app $APP_HOME

# change to the app user
USER app

# run entrypoint.prod.sh
ENTRYPOINT ["/home/app/web/entrypoint.prod.sh"]