import pandas as pd
from genpipes import declare
import json


@declare.processor()
def create_json_output(df: pd.DataFrame, output_name: str):
    """

    :param df:
    :param output_name:
    :return:
    """

    # json doesn't like datetime object so we transform it to into a readable object

    df['date'] = df['date'].dt.strftime('%Y-%d-%m')

    # create Dictionnary

    dic = df.groupby(['attcode', 'drug']).apply(lambda x: x[['date', 'id', 'title', 'type', 'journal']]
                                                .dropna()
                                                .to_dict('records')) \
        .reset_index() \
        .rename(columns={0: 'mentions'}) \
        .to_json(orient='records')

    with open(output_name, 'w', encoding='utf8') as output:
        json.dump(
            json.loads(dic),
            output,
            indent=2,
            sort_keys=True,
            ensure_ascii=False
        )

    return df
