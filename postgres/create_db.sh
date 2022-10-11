#!/usr/bin/env bash
set -e

## https://github.com/docker-library/postgres/issues/151

POSTGRES="psql --username ${POSTGRES_USER}"

echo "Creating databases"

$POSTGRES <<-EOSQL
CREATE DATABASE "${DB_API}" OWNER "${DB_USER}";
CREATE DATABASE "${DB_CORE}" OWNER "${DB_USER}";
EOSQL
