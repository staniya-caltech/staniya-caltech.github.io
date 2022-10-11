#!/usr/bin/env bash
set -e

## Enable some PostgreSQL extensions on DB_API

POSTGRES="psql --username=${POSTGRES_USER} --dbname=${DB_API}"

echo "Creating extensions on : ${DB_API}"

$POSTGRES <<EOSQL
CREATE EXTENSION IF NOT EXISTS "pgcrypto";
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "hstore";
EOSQL