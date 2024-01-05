from typing import Literal, TypedDict


class ConnectionProperty(TypedDict):
    '''
        Describes a connection property.
        https://cloud.google.com/bigquery/docs/reference/rest/v2/ConnectionProperty
    '''

    key: Literal['dataset_project_id', 'time_zone', 'session_id', 'query_label']
    value: str
