#!/usr/bin/env bash
set -e

## https://github.com/docker-library/postgres/issues/151

POSTGRES="psql --username ${POSTGRES_USER}"

echo "Creating database role: ${DB_USER}"

$POSTGRES <<-EOSQL
CREATE USER "${DB_USER}" WITH CREATEDB PASSWORD '${DB_PASS}';
EOSQL
