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
    :param drugs_files:
    :param stream:
    :return:
    """

    drugs = read_csv_files(drugs_files)

    for df in stream:
        mentions = [
            df[
                (df['title'].str.upper().str.contains(drug, case=False, na=False))
            ]
            .assign(drug=drug)
            for drug in drugs
        ]
        mentions_df = pd.concat(mentions)

        yield mentions_df

