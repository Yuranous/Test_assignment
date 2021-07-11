from abc import ABC, abstractmethod
from typing import List, Optional

import pandas as pd
from pandas import Series, DataFrame

filepath = 'res/signatures.tsv'


class Repository(ABC):
    @abstractmethod
    def get_data(self,
                 signature_ids: List[str] = None,
                 fields: List[str] = None,
                 ):
        pass

    @abstractmethod
    def get_fields(self):
        pass

    @abstractmethod
    def get_indices(self):
        pass

    @abstractmethod
    def get_stats(self,
                  signature_ids: List[str] = None,
                  fields: List[str] = None,
                  ):
        pass


class FileRepository(Repository):
    def __init__(self):
        self.df = pd.read_csv(filepath, sep='\t', index_col=0)

    def get_data(self,
                 signature_ids: List[str] = None,
                 fields: List[str] = None,
                 ):
        df = self.prepare_dataframe(self.df, indices=signature_ids, columns=fields)
        return df

    def get_fields(self):
        df = self.df

        return self.get_list(df.columns)

    def get_indices(self):
        df = self.df

        return self.get_list(df.index)

    def get_stats(self,
                  signature_ids: Optional[List[str]] = None,
                  fields: Optional[List[str]] = None
                  ):
        df = self.prepare_dataframe(self.df, indices=signature_ids, columns=fields)

        return df.describe()

    @staticmethod
    def get_list(series: Series):
        return list(series)

    @staticmethod
    def prepare_dataframe(
            df: DataFrame,
            indices: Optional[List[str]] = None,
            columns: Optional[List[str]] = None,
    ):
        if columns:
            df = df[columns]
        if indices:
            df = df.loc[indices]

        return df
