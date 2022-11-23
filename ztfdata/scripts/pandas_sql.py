import numpy as np
from ztfdata.models import PandasData
from .parse_fp import DataRetrieval
# Create your views here.
# Create your models here.
from django.db import models
from django.conf import settings
from django.core.management.base import BaseCommand

import pandas as pd
import psycopg2
from sqlalchemy import create_engine

class DataIngestion(BaseCommand):
    """ Data ingestion class extracts data from Pandas dataframes and imports it to a SQL for immediate use"""
    def __new__(cls, *args, **kwargs):
        """ Create a new instance of DataIngestion """
        return super().__new__(cls)

    def __init__(self, rel_filepath, pipeline):
        """ Parametrized constructor for DataIngestion Class """
        # Initialize a DataRetrieval object using the filepath as a parameter
        self.pipeline = pipeline
        self.rel_filepath = rel_filepath
        dr = DataRetrieval(self.rel_filepath, self.pipeline)
        if self.pipeline == "a":
            self.dataframe = dr.process_phot()
        else:
            self.dataframe = dr.process_dat()
        assert (type(self.dataframe) == pd.core.frame.DataFrame)
        self.dataframe = self.dataframe.replace('null', np.nan, regex=True)

    def clean_df_andrew(self):
        """"
        A function to prepare the dataframe for Andrew before converting to PostgresDB 
        """
        # self.dataframe.dropna()
        return self.dataframe

    def clean_df_mroz(self):
        """"
        A function to prepare the dataframe for Mrozpipe before converting to PostgresDB 
        """
        # self.dataframe.dropna(subset=['pid', 'bjd', 'mag', 'magerr', 'diffimflux',
        #                       'diffimfluxunc', 'clrcoeff', 'clrcoeffunc', 'infobits'])
        return self.dataframe

    def clean_df_ztffps(self):
        """"
        A function to prepare the dataframe for ztffps before converting to PostgresDB 
        """
        # self.dataframe.dropna(subset=['pid', 'jd', 'nearestrefmag', 'nearestrefmagunc',
        #                    'forcediffimflux', 'forcediffimfluxunc', 'clrcoeff', 'clrcoeffunc', 'infobitssci'])
        return self.dataframe

    def process_pandas_to_sql(self):
        """
        Function to convert Pandas DataFrame to Postgres DB by authenticating using information in .env and using Pandas.sql method
        """
        if self.pipeline == "a":
            self.clean_df_andrew()
        elif self.pipeline == "m":
            self.clean_df_mroz()
        elif self.pipeline == "z":
            self.clean_df_ztffps()
        else:
            raise Exception(
                "The input is not a product of a valid photometry pipeline")
        # establish connection to PostgreSQL by reading fields from Django settings
        user = settings.DATABASES['default']['USER']
        password = settings.DATABASES['default']['PASSWORD']
        database_name = settings.DATABASES['default']['NAME']
        host = settings.DATABASES['default']['HOST']
        port = settings.DATABASES['default']['PORT']
        conn_string = f'postgresql://{user}:{password}@{host}:{port}/{database_name}'
        engine = create_engine(conn_string, echo=False)
        self.dataframe.to_sql(PandasData._meta.db_table, con=engine, if_exists='append', index=False)
        return self.dataframe