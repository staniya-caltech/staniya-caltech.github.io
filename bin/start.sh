#!/usr/bin/env bash

docker-compose -f docker-compose.yaml -f development.yaml --project-name=dev up -d
