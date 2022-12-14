import numpy as np
import os
from .parse_fp import DataRetrieval

# Create your views here.
# Create your models here.
from django.conf import settings
from django.core.management.base import BaseCommand
from fpdata.models import ZTFFPSData, MROZData, AndrewData
import pandas as pd
import psycopg2
from psycopg2 import extras
from psycopg2.extensions import AsIs

import multiprocessing


class DataIngestion(BaseCommand):
    """Data ingestion class extracts data from Pandas dataframes and imports it to a SQL for immediate use"""

    def __new__(cls, *args, **kwargs):
        """Create a new instance of DataIngestion"""
        return super().__new__(cls)

    def __init__(self, rel_filepath, pipeline):
        """Parametrized constructor for DataIngestion Class"""
        # Initialize a DataRetrieval object using the filepath as a parameter
        self.pipeline = pipeline
        self.rel_filepath = rel_filepath
        dr = DataRetrieval(self.rel_filepath, self.pipeline)
        if self.pipeline == "a":
            self.dataframe = dr.process_phot()
        else:
            self.dataframe = dr.process_dat()
        assert isinstance(self.dataframe, pd.DataFrame)
        self.dataframe = self.dataframe.replace("null", np.nan, regex=True)

        # establish connection to PostgreSQL by reading fields from Django settings
        self.user = settings.DATABASES["default"]["USER"]
        self.password = settings.DATABASES["default"]["PASSWORD"]
        self.database_name = settings.DATABASES["default"]["NAME"]
        self.host = settings.DATABASES["default"]["HOST"]
        self.port = settings.DATABASES["default"]["PORT"]

    def prep_df_andrew(self):
        """ "
        A function to prepare the dataframe for Andrew before converting to PostgresDB
        """
        uniq_id = self.dataframe["PS1_ID"]
        return uniq_id

    def prep_df_mroz(self):
        """ "
        A function to prepare the dataframe for Mrozpipe before converting to PostgresDB
        """
        # Parse PS1_ID to get unique identifier
        uniq_id = os.path.basename(self.rel_filepath)[:-4].split("_")[1]
        return uniq_id

    def prep_df_ztffps(self):
        """ "
        A function to prepare the dataframe for ztffps before converting to PostgresDB
        """
        self.dataframe.drop("index", axis=1, inplace=True)

        # To get the magnitude, do not sum the forcediffumflux + nearest magnitude
        # Look at the documentation to understand how to get the magnitude for difference images

        # Parse PS1_ID to get unique identifier
        # _, PS1_ID, ccd, quad = os.path.basename(
        #     self.rel_filepath)[:-4].split("_")
        uniq_id = os.path.basename(self.rel_filepath)[:-4].split("_")[1]
        return uniq_id

    def executeQuery(self, query):
        """
        Function to run a query in PostgreSQL
        """
        conn = None
        try:
            conn = psycopg2.connect(
                host=self.host,
                port=self.port,
                database=self.database_name,
                user=self.user,
                password=self.password,
            )
            cursor = conn.cursor()
            # run a single query that is part of the query array
            cursor.execute(query)
            # close communication with the PostgreSQL database server
            cursor.close()
            # commit the changes
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

    def postgresqlInsertQuery(self, sql_command):
        """
        Function to append pandas data to postgresql
        """
        conn = None
        try:
            conn = psycopg2.connect(
                host=self.host,
                port=self.port,
                database=self.database_name,
                user=self.user,
                password=self.password,
            )
            cursor = conn.cursor()
            # run a single query that is part of the query array
            extras.execute_values(
                cur=cursor, sql=sql_command, argslist=self.dataframe.values
            )
            # close communication with the PostgreSQL database server
            cursor.close()
            # commit the changes
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

    def process_pandas_to_sql(self):
        """
        Function to convert Pandas DataFrame to Postgres DB by authenticating using information in .env and using Pandas.sql method
        """
        param = (AsIs("STARS"), AsIs(settings.DATABASES["default"]["USER"]))
        initial_query = (
            f"""CREATE SCHEMA IF NOT EXISTS {param[0]} AUTHORIZATION {param[1]};"""
        )
        self.executeQuery(initial_query)
        queries = []
        if self.pipeline == "a":
            uniq_id = self.prep_df_andrew()
            # TODO: Change table name to uniq_id
            insert_query_execute_val = f"""INSERT INTO {AsIs(AndrewData._meta.db_table)} IF NOT EXISTS (PS1_ID, MJD, Mag_ZTF, Mag_err, Flux, Flux_err, g_PS1, r_PS1, i_PS1, Stargal) values %s """  # type: ignore
            queries.append(insert_query_execute_val)
        elif self.pipeline == "m":
            uniq_id = self.prep_df_mroz()
            insert_query_execute_val = f"""INSERT INTO{AsIs(MROZData._meta.db_table)} IF NOT EXISTS(
                index, field, ccdid, qid, filter, pid, infobitssci, sciinpseeing, scibckgnd, scisigpix, zpmaginpsci, zpmaginpsciunc, zpmaginpscirms, clrcoeff, clrcoeffunc, ncalmatches, exptime, adpctdif1, adpctdif2, diffmaglim, zpdiff, programid, jd, rfid, forcediffimflux, forcediffimfluxunc, forcediffimsnr, forcediffimchisq, forcediffimfluxap, forcediffimfluxuncap, forcediffimsnrap, aperturecorr, dnearestrefsrc, nearestrefmag, nearestrefmagunc, nearestrefchi, nearestrefsharp, refjdstart, refjdend, procstatus) values %s """
            queries.append(insert_query_execute_val)
        elif self.pipeline == "z":
            uniq_id = self.prep_df_ztffps()
            insert_query_execute_val = f"""INSERT INTO {AsIs(ZTFFPSData._meta.db_table)} IF NOT EXISTS (
                bjd, mag, magerr, diffimflux, diffimfluxunc, flag, filterid, exptime, pid, field, ccd, quad, status, infobits, seeing, zpmagsci, zpmagsciunc, zpmagscirms, clrcoeff, clrcoeffunc, maglim, airmass, nps1matches) values %s """
            queries.append(insert_query_execute_val)
        else:
            raise Exception("The input is not a product of a valid photometry pipeline")

        # Parallelize the processes so that queries executie quicker
        N_CPU = 3
        pool = multiprocessing.Pool(N_CPU)
        for _ in pool.imap_unordered(self.postgresqlInsertQuery, queries):
            continue
