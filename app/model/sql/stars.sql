-- strategy for loading data --> unlogged data without any indices applied
-- load data afterwards --> cluster data
-- time constraint --> figuring out the indices for each of the columns


-- bulk upload data --> upload data first and do indices afterwards
-- turn off transaction logging

SET default_tablespace = stars_data_02;

    
CREATE TABLE stars (
    strid bigint NOT NULL,           -- Unique object identifier from original PS1 catalog
    ra double precision NOT NULL,    -- Right ascension [deg]
    dec double precision NOT NULL,   -- Declination [deg]
    gmeanpsfmag real NOT NULL,       -- Magnitude in g band [mag]
    rmeanpsfmag real NOT NULL,       -- Magnitude in r band [mag]
    imeanpsfmag real NOT NULL,       -- Magnitude in i band [mag]
    zmeanpsfmag real NOT NULL,       -- Magnitude in z band [mag]
    score real NOT NULL              -- Galaxy/star score (0..1); higher => more stellar
); 

ALTER TABLE stars OWNER TO ztfpo;

ALTER TABLE IF NOT EXISTS pipeline.stars SET SCHEMA transients;


SET default_tablespace = stars_indx_04;


ALTER TABLE ONLY stars
    ADD CONSTRAINT stars_pkey PRIMARY KEY (strid);


ALTER TABLE ONLY stars
    ADD CONSTRAINT stars_ra_check CHECK ((ra >= 0.0) AND (ra < 360.0));


ALTER TABLE ONLY stars
    ADD CONSTRAINT stars_dec_check CHECK ((dec >= -90.0) AND (dec <= 90.0));

CREATE index stars_gmeanpsfmag_idx on stars(gmeanpsfmag);
CREATE index stars_rmeanpsfmag_idx on stars(rmeanpsfmag);
CREATE index stars_imeanpsfmag_idx on stars(imeanpsfmag);
CREATE index stars_zmeanpsfmag_idx on stars(zmeanpsfmag);
CREATE index stars_score_idx on stars(score);

CREATE INDEX stars_radec_idx ON stars (q3c_ang2ipix(ra, dec));
CLUSTER stars_radec_idx ON stars;
ANALYZE stars;


REVOKE ALL ON TABLE stars FROM ztfpo;
GRANT INSERT,SELECT,UPDATE,DELETE,REFERENCES,TRIGGER ON TABLE stars TO ztfpo;





-- Return match with the closest Stars record
-- within the specified search radius.
--
create function getClosestMatchingStarToSkyPosition (
    ra_     double precision,
    dec_    double precision,
    radius_ real
)
    returns bigint as $$

    declare

        strId_            bigint;

    begin

        strId_  := null;

        select strId
        into strId_
        from Stars
        where q3c_radial_query(ra, dec, ra_, dec_, radius_)
        order by q3c_dist(ra_, dec_, ra, dec)
        limit 1;

        if (strId_ is null) then

            strId_ := -1;

        end if;

        return strId_;

    end;

$$ language plpgsql;
