import pandas as pd
from typing import Callable
from genpipes import declare
from src.jobs.extractor.read_json import read_json_files
from src.jobs.extractor.read_csv import read_csv_files


@declare.generator(inputs=[read_csv_files, read_json_files])
def merge_files(
        read_csv_files: Callable,
        read_json_files: Callable,
        csv_files: list,
        json_files: list
) -> pd.DataFrame:
    """
    :param read_csv_files:
    :param read_json_files:
    :param csv_files:
    :param json_files:
    :return:
    """

    csv_df = read_csv_files(files=csv_files)
    json_df = read_json_files(files=json_files)

    df = pd.concat([csv_df, json_df])
    return df
