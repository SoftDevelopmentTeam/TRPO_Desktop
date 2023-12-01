@echo off

docker-compose -f ..\docker\docker-compose.build.yml up
copy ..\app\client_secrets.json ..\dist\