import csv
import os


class DataRetrieval:
    """ Data retrieval class extracts data from different forced photometry pipelines"""

    def __init__(self, filepath):
        """ Run data_extraction function depending on filename"""
        self.filepath = filepath
        assert (os.path.exists(self.filepath))
        self.filename = os.path.basename(filepath)
        if "ps1" in self.filename:
            self.pipeline = "a"
        elif "mrozpipe" in self.filename:
            self.pipeline = "m"
        elif "zttfps" in self.filename:
            self.pipeline = "z"
        else:
            print("The file you inputted was not valid. Please input a filepath for a file that was generated through one of the three approved forced photometry pipelines. ")

    def process_dat(self):
        """
        Function to parse contents of dat file and write it as a csv
        """
        assert (os.path.splitext(self.filepath[-1].lower == ".dat"))
        # read flash.dat to a list of lists
        datContent = [i.strip().split()
                      for i in open(self.filepath).readlines()]
        output_csv = os.path.dirname(
            self.filepath) + self.filename.split(".", 1)[0] + ".csv"
        print(output_csv)
        # write contents as a new CSV file
        with open(output_csv, "wb") as f:
            writer = csv.writer(f)
            writer.writerows(datContent)


def main():
    # Testing dataretrieval class
    data = DataRetrieval(
        "/Users/staniya/Documents/Schmidt Academy/ZTF/lightcurves/ztffps/ztffps_192331646755804879_0842_38.dat")
    if data.pipeline == "z":
        data.process_dat()


if __name__ == "__main__":
    main()
