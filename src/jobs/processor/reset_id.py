import pandas as pd
from typing import Iterable
from genpipes import declare


def reset_id(stream: Iterable[pd.DataFrame]):
    """
    Reset id column

    This function resets the id column.
    :param stream: Iterable[pd.DataFrame]
        Stream of dataframes.
    :return: df: pd.DataFrame
        Dataframe containing the reformatted data.
    """

    for df in stream:
        df_id = df.reset_index() \
            .drop(columns=['id']) \
            .rename(columns={'index': 'id'})

        yield df_id
