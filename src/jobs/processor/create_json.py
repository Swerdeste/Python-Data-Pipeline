import pandas as pd
import json
from genpipes import declare
from typing import Iterator


@declare.processor()
def create_json(
        stream: Iterator[pd.DataFrame],
        output_path: str):
    """
    Create a json file from a dataframe.

    This function create our json representation of the dataframe and save it locally.

    :param stream: Iterator[pd.DataFrame]
        The stream of dataframes to process.
    :param output_path: str
        The filepath to save the json file.

    :return: df : Iterator[pd.DataFrame]
        The stream of dataframes.

    """

    for df in stream:

        # json doesn't like datetime object so we transform it to into a readable object
        df['date'] = pd.to_datetime(df['date'])
        df['date'] = df['date'].dt.strftime('%Y-%d-%m')

        # create a json-type object with drug appearances in articles

        dic = df.groupby(['drug']).apply(lambda x: x[['date', 'id', 'title', 'type', 'journal']]
                                                    .dropna()
                                                    .to_dict('records')) \
            .reset_index() \
            .rename(columns={0: 'mentions'}) \
            .to_json(orient='records')

        # save the json file locally

        with open(output_path, 'w', encoding='utf8') as output:
            json.dump(
                json.loads(dic),
                output,
                indent=2,
                sort_keys=True,
                ensure_ascii=False
            )

        yield df
