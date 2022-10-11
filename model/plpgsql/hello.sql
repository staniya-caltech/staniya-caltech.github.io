-- Example from
-- http://www.postgresonline.com/journal/archives/58-Quick-Guide-to-writing-PLPGSQL-Functions-Part-1.html

CREATE OR REPLACE FUNCTION fnsomefunc(numtimes INTEGER, msg TEXT)
  RETURNS TEXT AS
$$
DECLARE
  strresult TEXT;
BEGIN
  strresult := '';
  IF numtimes > 0
  THEN
    FOR i IN 1 .. numtimes LOOP
      strresult := strresult || msg || E'\r\n';
    END LOOP;
  END IF;
  RETURN strresult;
END;
$$
LANGUAGE 'plpgsql' IMMUTABLE
SECURITY DEFINER
COST 10;



-- To call the function we do this and it returns ten hello there's
-- with carriage returns as a single text field.
SELECT fnsomefunc(10, 'Hello there');