import json
import pandas as pd
from collections import Counter


def ad_hoc(json_file):
    with open(json_file) as f:
        data = pd.json_normalize(json.load(f), record_path=['mentions'], meta=['drug'])
    journal_with_most_drugs_quote = data.groupby('journal').drug.nunique()

    return journal_with_most_drugs_quote.loc[
        journal_with_most_drugs_quote == journal_with_most_drugs_quote.max()].index.tolist()

