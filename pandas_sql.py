import numpy as np
import pandas as pd
import plotly.express as px
import os

class DataIngestion:
    """ Data ingestion class extracts data from Pandas dataframes and imports it to a SQL for immediate use"""
    def __new__(cls, *args, **kwargs):
        """ Create a new instance of DataIngestion """
        return super().__new__(cls)

    def __init__(self, dataframe):
        """ Parametrized constructor for DataIngestion Class """
        self.dataframe = dataframe
        assert(type(self.dataframe == pd.core.frame.DataFrame))
    
    def data_processing(self):
        """ Process the dataframe such that it contains appropriate data"""
        self.dataframe.dropna(subset=[''])

def main():
    return

if __name__ == "__main__":
    main()