import pandas as pd
import numpy as np
import datetime as dt
from time import strftime
import src.extractor as extractor


class Transformer(extractor.Extractor):
    """
    Transformer class is used to transform the data
    """
    def __init__(self, path):
        super().__init__(path)
        self.out = {} # This is the output of the transformer
        self.name = path.split('/')[-1].split('\\')[-1].split('.')[0] # Get the name of the file

    def lower_case(self):
        """
        This function is used to lower case the strings in the dataframe
        :return:
        """
        self.df = self.df.applymap(lambda s: s.lower() if type(s) == str else s)
        return self.df

    def format_date(self):
        """
        This function is used to format the date column
        :return:
        """

        self.df['date'] = pd.to_datetime(self.df['date'])
        self.df['date'] = self.df['date'].dt.strftime('%d/%m/%Y')

    def find_drugs(self, drugs):
        """
        This function is used to find the drugs appearances in the title column
        :param drugs: List of drugs
        :return:
        """
        for drug in drugs:
            appearances = self.df[self.df['title'].str.contains(drug)]
            if not appearances.empty:
                results = appearances
                self.out[drug] = {self.name: results[['date', 'title','journal']].to_dict('records')}

    def change_title(self):
        """
        This function is used to change the name of the title column
        :return:
        """
        columns = self.df.columns
        for column in columns:
            if 'title' in column:
                self.df.rename(columns={column: 'title'}, inplace=True)

    def transform(self, drugs):
        """
        This function is used to run all the transformations
        :param drugs: List of drugs
        :return:
        """
        self.lower_case()
        self.change_title()
        self.format_date()
        self.find_drugs(drugs)


    def find_journal(self,drugs):
        """
        This function is used to find the journal appearances in the title column
        :param journal: List of journals
        :return:
        """
        for drug in drugs:
            appearances = self.df[self.df['title'].str.contains(drug)]
            if not appearances.empty:
                results = appearances
                self.out[drug] = {self.name: results[['date', 'title']].to_dict('records'),
                                  'journal': results[['date', 'journal']].to_dict('records')}