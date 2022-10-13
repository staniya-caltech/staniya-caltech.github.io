import csv

def dat_csv(filename):
    """
    Function to parse contents of dat file and write it as a csv
    """
    # read flash.dat to a list of lists
    datContent = [i.strip().split() for i in open(filename).readlines()]

    # write contents as a new CSV file
    
