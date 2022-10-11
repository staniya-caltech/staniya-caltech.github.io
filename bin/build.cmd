@echo off

docker rm postgres
docker rmi dev_postgres
docker-compose -f docker-compose.yaml -f development.yaml --project-name=dev build

pause