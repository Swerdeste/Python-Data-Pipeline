import json
from collections import Counter


def ad_hoc(json_file):
    with open(json_file) as f:
        data = json.load(f)
        for drug in data:
            for key in data[drug].keys():



