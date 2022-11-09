import pandas as pd
from genpipes import declare


@declare.datasource()
def read_csv_files(files: list) -> pd.DataFrame:
    """
    Read csv files and return a dataframe

    This function reads csv files and returns a dataframe.

    :param files: list(dict)
        List of dictionaries containing the parameters to read the files.
    :return: df: pd.DataFrame
        Dataframe containing the data from the csv files.

    """

    df = pd.concat(
        (
            pd.read_csv(**f['read_csv'])
            .assign(type=f['filename'])
            .rename(columns=f['columns_to_rename'])
            for f in files
        )
    )
    return df


