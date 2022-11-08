import pandas as pd
import numpy as np
import yaml
import json


class Extractor:
    """
    Extractor class is used to extract the data
    """
    def __init__(self, path):
        # This is the input of the extractor
        if path.endswith('.csv'): # If the file is a csv
            self.df = pd.read_csv(path)
        if path.endswith('.json'): # If the file is a json
            with open(path, 'r') as f:
                data = yaml.load(f, Loader=yaml.FullLoader) # Python doesn't support trailing commas in json,
                # but yaml package does
                self.df = pd.read_json(json.dumps(data))

    def extract(self, column):
        """
        This function is used to extract the data from a column and return a list of the values
        :param column: String of the column name
        :return:
        """
        return self.df[column].tolist()
