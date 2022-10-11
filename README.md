# docker-postgresql

This is the relational model development stack using PostgreSQL. [aka How to] Enterprise Data Modelling development with PostgreSQL, using Docker, from local development up to deliverable to the production deployment end. It uses the [official PostgreSQL docker image](https://github.com/docker-library/postgres) that can be found from [hub](https://hub.docker.com/_/postgres/) or [store](https://store.docker.com/images/postgres).

This does:

- create the DB user that defined in `development.yaml` and `create_user.sh`
- create multiple databases that defined in `development.yaml` and `create_db.sh`
- set the necessary DB users and password defined in `development.yaml` and `.env`
- create necessary PostgreSQL extensions defined in `create_extensions.sh`

It assumes:

- you have docker installed, up and running
- trivially on macOS get official [download for Desktop](https://www.docker.com/docker-mac) or `brew install docker`
- then prepare the environment variables

```
git clone https://github.com/victorskl/docker-postgresql.git
cd docker-postgresql
mkdir -p data
cp env.sample .env
```

### Quick Start

If you know what you are doing, here is TL;DR:

```
sed -i '' -e 's/#POSTGRES_USER/POSTGRES_USER/g' .env
sed -i '' -e 's/#DB_USER/DB_USER/g' .env
sed -i '' -e 's/#DB_API/DB_API/g' .env
sed -i '' -e 's/#DB_CORE/DB_CORE/g' .env
docker-compose -p dev up -d
```

### Running Foreground (Interactive)

```
docker-compose -f docker-compose.yaml -f development.yaml --project-name=dev build
docker-compose -f docker-compose.yaml -f development.yaml --project-name=dev up
```

- Enter

```
docker ps
docker exec -it postgres bash
su - postgres
psql
\l
\c db_api
SELECT * FROM pg_extension;
\q
exit
exit
```

- Stop

```
docker ps
docker-compose -f docker-compose.yaml -f development.yaml --project-name=dev down
```

- Recycle

```
docker ps -a
docker images -a
docker rm postgres
docker rmi dev_postgres
```

### Running Background (Daemon)

- Change `.cmd` to `.sh` if macOS or Linux.

```
(Windows)
PS D:\Projects\github\docker-postgresql> .\bin\build.cmd
PS D:\Projects\github\docker-postgresql> .\bin\start.cmd

(macOS)
bash bin/build.sh
bash bin/start.sh
```

- Enter into PostgreSQL container

```
PS D:\Projects\github\docker-postgresql> .\bin\enter.cmd
```

*PS denotes - PowerShell windows*

### Data Modeling

- Use favourite choice of DB Data Modeling tools
    
    - [pgAdmin](https://www.pgadmin.org/)
    - [DataGrip](https://www.jetbrains.com/datagrip/)
    - [SQLDeveloper](http://www.oracle.com/technetwork/developer-tools/sql-developer/downloads/index.html)
    - [pgModeler](https://github.com/pgmodeler/pgmodeler)
    
- Connect 

    ```
    Host: localhost
    Port: 5432
    Database: db_api
    Username: db_user
    Password: changeme
    ```

- Try sample data modelling in [/model](model)


### Production

- Expand and adapt this to prepare the necessary arrangement for your production environment.

- Check the [docker compose volumes](https://docs.docker.com/compose/compose-file/#volumes) setting to persist the PostgreSQL data - which is in [docker-compose.yaml](docker-compose.yaml) to `./data` directory 

    ```
        volumes:
          - ./data:/var/lib/postgresql/data
    ```