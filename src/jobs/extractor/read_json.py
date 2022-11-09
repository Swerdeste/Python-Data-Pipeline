import pandas as pd
from genpipes import declare
from src.utils.tools import loads_json


@declare.datasource()
def read_json_files(files: list) -> pd.DataFrame:
    """
    Read json files and return a dataframe

    This function reads json files and returns a dataframe.

    :param files: list(dict)
        List of dictionaries containing the parameters to read the files.
    :return: df: pd.DataFrame
        Dataframe containing the data from the json files.

    """

    df = pd.concat(
        (
            pd.DataFrame(loads_json(
                f['read_json']['filepath_or_buffer']
            ))
            .assign(type=f['filename'])
            .rename(columns=f['columns_to_rename'])
            for f in files
        )
    )
    return df
