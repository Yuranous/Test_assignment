import uvicorn
from fastapi import FastAPI, Depends

from data import FileRepository
from model import SignaturesQueryParams

app = FastAPI()
repository = FileRepository()


@app.get('/signatures')
def get_signatures(params: SignaturesQueryParams = Depends()):
    """
    Get all signatures matching specified criteria.
    """
    return repository.get_data(**params.to_dict())


@app.get('/signatures/stats')
def get_signatures_statistics(params: SignaturesQueryParams = Depends()):
    """
    Get statistical description of signatures matching specified criteria.
    """
    return repository.get_stats(**params.to_dict())


@app.get('/signatures/fields')
def signature_fields():
    """
    Get all fields (column names) from signatures
    """
    return repository.get_fields()


@app.get('/signatures/id')
def signature_indices():
    """
    Get all indices (labels) from signatures
    """
    return repository.get_indices()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
