import numpy as np
import pandas as pd
import plotly.express as px
import os
from parse_fp import DataRetrieval
from sqlalchemy import create_engine
import logging
from functools import partial

from dotenv import find_dotenv, dotenv_values


class DataIngestion:
    """ Data ingestion class extracts data from Pandas dataframes and imports it to a SQL for immediate use"""
    def __new__(cls, *args, **kwargs):
        """ Create a new instance of DataIngestion """
        return super().__new__(cls)

    def __init__(self, filepath):
        """ Parametrized constructor for DataIngestion Class """
        # Initialize a DataRetrieval object using the filepath as a parameter
        dr = DataRetrieval(filepath)
        self.pipeline = dr.pipeline
        if self.pipeline == "a":
            self.dataframe = dr.process_phot()
        else:
            self.dataframe = dr.process_dat()
        assert (type(self.dataframe == pd.core.frame.DataFrame))

    def clean_df_andrew(self):
        """"
        A function to prepare the dataframe for Andrew before converting to PostgresDB 
        """
        self.dataframe.dropna()
        return self.dataframe

    def clean_df_mroz(self):
        """"
        A function to prepare the dataframe for Mrozpipe before converting to PostgresDB 
        """
        self.dataframe.dropna(subset=['pid', 'bjd', 'mag', 'magerr', 'diffimflux',
                              'diffimfluxunc', 'clrcoeff', 'clrcoeffunc', 'infobits'])
        return self.dataframe

    def clean_df_ztffps(self):
        """"
        A function to prepare the dataframe for ztffps before converting to PostgresDB 
        """
        self.dataframe.dropna(subset=['pid', 'jd', 'nearestrefmag', 'nearestrefmagunc',
                              'forcediffimflux', 'forcediffimfluxunc', 'clrcoeff', 'clrcoeffunc', 'infobitssci'])
        return self.dataframe

    def populate_args_from_dotenv(self, func):
        """
        Function to read secret environment variables from .env file
        """
        logger = logging.getLogger(__name__)
        try:
            dotenv_path = find_dotenv(raise_error_if_not_found=True)
            logger.info('Found .evn, loading variables')
            env_dict = dotenv_values(dotenv_path=dotenv_path)
            par_func = partial(func, **env_dict)
            par_func.__doc__ = func.__doc__
            return par_func
        except IOError:
            logger.info('Didn\'t find .env')
            return func 

    def establish_sql_conn(self):
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
        self.populate_args_from_dotenv()    


def main():
    return


if __name__ == "__main__":
    main()
