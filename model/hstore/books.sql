-- hstore tutorial from
-- http://www.postgresqltutorial.com/postgresql-hstore/

CREATE TABLE books (
  id    SERIAL PRIMARY KEY,
  title VARCHAR(255),
  attr  HSTORE
);

INSERT INTO books (title, attr) VALUES (
  'PostgreSQL Tutorial',
  '"paperback" => "243",
     "publisher" => "postgresqltutorial.com",
     "language"  => "English",
     "ISBN-13"   => "978-1449370000",
  "weight"    => "11.2 ounces"'
);

-- Query data from a hstore column
SELECT attr
FROM books;

-- Query value for a specific key using -> operator
SELECT attr -> 'ISBN-13' AS isbn
FROM books;

-- Use value in the WHERE clause
-- use the -> operator in the WHERE clause to filter the rows
-- whose values of the hstore column match the input value.
SELECT attr -> 'weight' AS weight
FROM books
WHERE attr -> 'ISBN-13' = '978-1449370000';

-- Add key-value pairs to existing rows
UPDATE books
SET attr = attr || '"freeshipping"=>"yes"' :: HSTORE;

SELECT
  title,
  attr -> 'freeshipping' AS freeshipping
FROM books;

-- Update existing key-value pair
UPDATE books
SET attr = attr || '"freeshipping"=>"no"' :: HSTORE;

-- Remove existing key-value pair
UPDATE books
SET attr = delete(attr, 'freeshipping');

-- Check for a specific key in hstore column
SELECT
  title,
  attr -> 'publisher' AS publisher,
  attr
FROM
  books
WHERE
  attr ? 'publisher';

-- Check for a key-value pair
SELECT title
FROM
  books
WHERE
  attr @> '"weight"=>"11.2 ounces"' :: HSTORE;

-- Query rows that contain multiple specified keys
SELECT title
FROM
  books
WHERE
  attr ?& ARRAY ['language', 'weight'];

-- Get all keys from a hstore column
SELECT akeys(attr)
FROM
  books;

SELECT skeys(attr)
FROM
  books;

-- Get all values from an hstore column
SELECT avals(attr)
FROM
  books;

SELECT svals(attr)
FROM
  books;

-- Convert hstore data to JSON
SELECT
  title,
  hstore_to_json(attr) json
FROM
  books;

-- Convert hstore data to sets
SELECT
  title,
  (EACH(attr)).*
FROM
  books;

-- More:
-- http://postgresguide.com/cool/hstore.html
-- https://www.postgresql.org/docs/9.6/static/hstore.html