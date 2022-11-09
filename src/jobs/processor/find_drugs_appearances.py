import pandas as pd
from typing import Iterable, Callable
from genpipes import declare
from src.jobs.extractor.read_csv import read_csv_files


@declare.processor()
def find_drugs_appearances(
        stream: Iterable[pd.DataFrame],
        drugs_files: list[dict]
):
    """
    Find drugs appearances in the dataframe

    This function finds the drugs appearances in the dataframe.

    :param read_csv_files: Callable
        Function to read csv files.
    :param drugs_files: list(dict)
        List of dictionaries containing the parameters to read the files.
    :param stream: Iterable[pd.DataFrame]
        Stream of dataframes.

    :return: df: pd.DataFrame
         Dataframe containing the reformatted data.
    """

    drugs = read_csv_files(files=drugs_files)

    for df in stream:
        mentions = [
            df[
                (df['title'].str.upper().str.contains(drug, case=False, na=False))
            ]
            .assign(drug=drug)
            for drug in drugs.drug
        ]
        mentions_df = pd.concat(mentions)

        yield mentions_df

