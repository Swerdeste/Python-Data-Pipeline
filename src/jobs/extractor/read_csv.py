import pandas as pd
from genpipes import declare


@declare.datasource()
def read_csv_files(files: list) -> pd.Dataframe:
    """

    :param files:
    :return:
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


