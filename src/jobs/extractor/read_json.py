import pandas as pd
from genpipes import declare
from src.utils.tools import loads_json


@declare.datasource()
def read_json_files(files: list) -> pd.DataFrame:
    """

    :param files:
    :return:
    """
    df = pd.concat(
        (
            pd.DataFrame(loads_json(
                f['file']
            ))
            .assign(type=f['filename'])
            .rename(columns=f['columns_to_rename'])
            for f in files
        )
    )
    return df
