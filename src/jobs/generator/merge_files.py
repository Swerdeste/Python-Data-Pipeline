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
    Merge csv and json files

    This function merges csv and json files into a single dataframe.

    :param read_csv_files: Callable
        Function to read csv files from extractor module
    :param read_json_files: Callable
        Function to read json files from extractor module
    :param csv_files: list of dict
        Configuration of csv files to read
    :param json_files: list of dict
        Configuration of json files to read

    :return: df: pd.DataFrame
        Merged dataframe
    """

    csv_df = read_csv_files(files=csv_files)
    json_df = read_json_files(files=json_files)

    df = pd.concat([csv_df, json_df])  # Concatenate dataframes

    return df
