from typing import TypedDict, Dict, List, Optional

class TimePartitioning(TypedDict):
    '''
        Describes time-based partitioning specification for a table.
        https://cloud.google.com/bigquery/docs/reference/rest/v2/tables#TimePartitioning
    '''
    
    type: str
    expiration_ms: str
    field: str
    require_partition_filter: bool


class Range(TypedDict):
    '''
        Describes range specification for a range partitioning specification.
        https://cloud.google.com/bigquery/docs/reference/rest/v2/tables#TimePartitioning
    '''

    start: str
    end: str
    interval: str

class RangePartitioning(TypedDict):
    '''
        Describes range partitioning specification for a table.
        https://cloud.google.com/bigquery/docs/reference/rest/v2/tables#RangePartitioning
    '''

    field: str
    range: Range

class Clustering(TypedDict):
    '''
        Describes clustering specification for a table.
        https://cloud.google.com/bigquery/docs/reference/rest/v2/tables#Clustering
    '''

    fields: List[str]

class ErrorProto(TypedDict):
    '''
        Describes error details.
        https://cloud.google.com/bigquery/docs/reference/rest/v2/tables#ErrorProto
    '''

    reason: str
    location: str
    debug_info: str
    message: str
