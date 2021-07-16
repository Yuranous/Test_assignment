from typing import List

from pydantic import BaseModel, Field


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
