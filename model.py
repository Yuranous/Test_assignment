from typing import Optional

from fastapi import Query


class SignaturesQueryParams:
    def __init__(
            self,
            ids: Optional[str] = Query(
                None,
                description="Comma-separated list of signatures' IDs that should be shown in response",
                regex='^(NSCLC\S\d*\S,?)*[^\s,]$',
            ),
            fields: Optional[str] = Query(
                None,
                description="Comma-separated list of fields that should be shown in response",
                regex='^[^\s,](\w*\S,?\S)*[^\s,]$',
            )
    ):
        self.ids = ids
        self.fields = fields

    def to_dict(self):
        kwargs = {}

        if self.ids:
            kwargs['signature_ids'] = self.ids.split(',')
        if self.fields:
            kwargs['fields'] = self.fields.split(',')

        return kwargs
