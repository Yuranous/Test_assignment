from enum import Enum
from typing import Optional, List

from fastapi import Query
from pydantic import BaseModel, Field


# class DataFormat(str, Enum):
#     split = 'split'
#     records = 'records'
#     index = 'index'
#     values = 'values'
#     table = 'table'


class FieldModel(BaseModel):
    name: str
    type: str


class SchemaModel(BaseModel):
    primary_key: List[str] = Field(None, alias='primaryKey')
    pandas_version: str
    fields: List[FieldModel]


class DataFrameModel(BaseModel):
    dataframe_schema: SchemaModel = Field(None, alias='schema')
    data: List[dict]


class FieldListModel(BaseModel):
    fields: List[FieldModel]


class IndexListModel(BaseModel):
    indices: List[str]
