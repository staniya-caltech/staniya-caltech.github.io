
# Local Test for DataRetrieval
# def test_data_retrieval(data_list):
#     for data in data_list:
#         data = pandas_sql.DataRetrieval(data)

#         if data.pipeline == "a":
#             andrew_dataframe=data.process_phot()
#             print(andrew_dataframe.head())
#             print(andrew_dataframe.isnull().sum())
#             print(andrew_dataframe.dtypes)
#         else:
#             other_dataframe=data.process_dat()
#             print(other_dataframe.head())
#             print(other_dataframe.isnull().sum())
#             print(other_dataframe.dtypes)

from pandas_sql import DataIngestion


def test_data_ingestion(data_list):
    for data in data_list:
        data = DataIngestion(data)
        df = data.process_pandas_to_sql()
        print(df.head())
        print(df.isnull().sum())
        print(df.dtypes)

def main():
    # Testing dataretrieval class
    data_list = [
        "/Users/staniya/Documents/Schmidt Academy/ZTF/Data/lightcurves/Andrew/ps1_sources_0842_38_zr_sciimg.phot",
        "/Users/staniya/Documents/Schmidt Academy/ZTF/Data/lightcurves/mrozpipe/mrozpipe_156790468415434435_0699_38.dat",
        "/Users/staniya/Documents/Schmidt Academy/ZTF/Data/lightcurves/ztffps/ztffps_156800463984462670_0699_38.dat"
    ]
    # test_data_retrieval(data_list)

    # Testing dataingestion class
    test_data_ingestion(data_list)


if __name__ == "__main__":
    main()