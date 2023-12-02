#!/bin/bash

printf "\n\n%s\n" "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
printf "%-59s" "+ Building program "; printf "%s\n" "+"
printf "\n\n%s\n" "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"

docker-compose -f ../docker/docker-compose.build.yml up
cp ../app/client_secrets.json ../dist/
