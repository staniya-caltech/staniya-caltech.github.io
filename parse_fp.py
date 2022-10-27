import os
import pandas as pd


class DataRetrieval:
    """ Data retrieval class extracts data from different forced photometry pipelines"""
    def __new__(cls, *args, **kwargs):
        """ Create a new instance of DataRetrieval """
        return super().__new__(cls)

    def __init__(self, filepath):
        """ Run data_extraction function depending on filename"""
        self.filepath = filepath
        assert (os.path.exists(self.filepath))
        self.filename = os.path.basename(filepath)
        self.returnlist = []
        if "ps1" in self.filename:
            self.pipeline = "a"
        elif "mrozpipe" in self.filename:
            self.pipeline = "m"
        elif "ztffps" in self.filename:
            self.pipeline = "z"
        else:
            raise Exception(
                "The input is not a product of a valid photometry pipeline")

    def process_phot(self):
        """
        Function to parse contents of phot file and write it as a csv
        """
        assert (os.path.splitext(self.filepath)[-1].lower() == ".phot")
        header = ["PS1_ID", "MJD", "Mag_ZTF", "Mag_err", "Flux",
                  "Flux_err", "g_PS1", "r_PS1", "i_PS1", "Stargal", "infobits"]

        # read the contents of .phot file as a list of strings, then create a csv by replacing the whitespaces of each string with commas
        with open(self.filepath, "r") as in_file:
            mod_file = list(in_file)
            for i, line in enumerate(mod_file):
                mod_file[i] = line.strip().split(" ")
        return pd.DataFrame(mod_file, columns=header)

    def process_dat(self):
        """
        Function to parse contents of dat file and write it as a csv
        """
        assert (os.path.splitext(self.filepath)[-1].lower() == ".dat")

        # read flash.dat to a list of lists
        datContent = [i.strip().split()
                      for i in open(self.filepath).readlines()]
        for content_i in reversed(range(len(datContent))):
            if datContent[content_i][0] == "#":
                del datContent[content_i]
        # remove the unnecessary commas in header row
        header_row = [param.replace(',', '') for param in datContent[0]]
        datContent = datContent[1:]
        return pd.DataFrame(datContent, columns=header_row)
