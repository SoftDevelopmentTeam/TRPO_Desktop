#!/bin/bash

docker-compose -f ../docker/docker-compose.build.yml up
cp ../app/client_secrets.json ../dist/
