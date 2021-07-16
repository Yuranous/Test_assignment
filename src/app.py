from typing import Optional, List

from fastapi import FastAPI, Depends, Query

from src.data import FileRepository
from src.model import DataFrameModel, FieldListModel, IndexListModel

app = FastAPI()
repository = FileRepository()


# @app.get('/signatures', response_model=DataFrameModel)
# def get_signatures(params: SignaturesQueryParams = Depends()):
#     """
#     Get all signatures matching specified criteria.
#     """
#     return repository.get_data(**params.to_dict())

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
    return repository.get_data(ids, fields)


@app.get('/signatures/stats')
def get_signatures_statistics(
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
    Get statistical description of signatures matching specified criteria.
    """
    return repository.get_stats(ids, fields)


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
