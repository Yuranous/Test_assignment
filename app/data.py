import json
from abc import ABC, abstractmethod
from typing import List, Optional

import pandas as pd
from pandas import DataFrame

from .settings import FILE_PATH, FILE_SEPARATOR


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
        self.df = pd.read_csv(FILE_PATH, sep=FILE_SEPARATOR, index_col=0)

    def get_data(self,
                 signature_ids: List[str] = None,
                 fields: List[str] = None,
                 ):
        df = self.prepare_dataframe(self.df, indices=signature_ids, columns=fields)
        return json.loads(df.to_json(orient="table"))

    def get_fields(self):
        return [
            {
                'name': str(column),
                'type': str(data.dtype),
            }
            for column, data in self.df.iteritems()
        ]

    def get_indices(self):
        return list(self.df.index)

    def get_stats(self,
                  signature_ids: Optional[List[str]] = None,
                  fields: Optional[List[str]] = None
                  ):
        df = self.prepare_dataframe(self.df, indices=signature_ids, columns=fields)

        return json.loads(df.describe().to_json(orient='table'))

    @staticmethod
    def prepare_dataframe(
            df: DataFrame,
            indices: Optional[List[str]] = None,
            columns: Optional[List[str]] = None,
    ):
        if columns:
            try:
                df = df[columns]
            except KeyError as e:
                raise KeyError("Invalid column name provided")
        if indices:
            try:
                df = df.loc[indices]
            except KeyError as e:
                raise KeyError("Invalid index provided")

        return df
