import csv


class DataRetrieval:
    """ Data retrieval class extracts data from different forced photometry pipelines"""

    def __init__(self, pipeline_name):
        """ Run data_extraction function depending on pipeline_name"""
        self.pipeline_name = pipeline_name

    def dat_csv(filename, output_csv):
        """
        Function to parse contents of dat file and write it as a csv
        """
        # read flash.dat to a list of lists
        datContent = [i.strip().split() for i in open(filename).readlines()]

        # write contents as a new CSV file
        with open(output_csv, "wb") as f:
            writer = csv.writer(f)
            writer.writerows(datContent)

    def main():
        


sample_filename = "~/Documents/Schmidt\ Academy/ZTF/lightcurves/ZTF/lightcurves/ztffps"
data_csv(sample_filename, "../")
