from typing import Optional, List

from fastapi import FastAPI, Query, HTTPException

from .data import FileRepository
from .models import DataFrameModel, FieldListModel, IndexListModel

app = FastAPI()
repository = FileRepository()


def clear_list_from_blank(data: List):
    return [i for i in data if i]


@app.get('/signatures', response_model=DataFrameModel)
def get_signatures(
        ids: Optional[List[str]] = Query(
            None,
            description="List of signatures' IDs that should be shown in response",
        ),
        fields: Optional[List[str]] = Query(
            None,
            description="List of fields that should be shown in response",
        )
):
    """
    Get all signatures matching specified criteria.
    """
    ids = clear_list_from_blank(ids) if ids else ids
    fields = clear_list_from_blank(fields) if fields else fields
    try:
        return repository.get_data(ids, fields)
    except KeyError as e:
        raise HTTPException(status_code=406, detail=str(e))


@app.get('/signatures/stats', response_model=DataFrameModel)
def get_signatures_statistics(
        ids: Optional[List[str]] = Query(
            None,
            description="List of signatures' IDs that should be used in the statistical computation",
        ),
        fields: Optional[List[str]] = Query(
            None,
            description="List of fields that should be used in the statistical computation",
        )
):
    """
    Get statistical description of signatures matching specified criteria.
    """
    ids = clear_list_from_blank(ids) if ids else ids
    fields = clear_list_from_blank(fields) if fields else fields
    try:
        return repository.get_stats(ids, fields)
    except KeyError as e:
        raise HTTPException(status_code=406, detail=str(e))


@app.get('/signatures/fields', response_model=FieldListModel)
def signature_fields():
    """
    Get all fields (column names) from signatures
    """
    return {
        'fields': repository.get_fields()
    }


@app.get('/signatures/ids', response_model=IndexListModel)
def signature_indices():
    """
    Get all indices (labels) from signatures
    """
    return {
        'indices': repository.get_indices()
    }
