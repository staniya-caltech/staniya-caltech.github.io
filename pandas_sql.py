import numpy as np
import pandas as pd
import plotly.express as px
import os
from parse_fp import DataRetrieval

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
            self.dataframe=dr.process_phot()
        else:
            self.dataframe=dr.process_dat()
        assert(type(self.dataframe == pd.core.frame.DataFrame))
    
    def data_processing(self):
        """ Process the dataframe such that it contains appropriate data"""
        self.dataframe.dropna(subset=[''])

def main():
    return

if __name__ == "__main__":
    main()