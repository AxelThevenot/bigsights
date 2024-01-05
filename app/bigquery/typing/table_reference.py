from typing import TypedDict, Dict, List, Optional

class TableReference(TypedDict):
    '''
        Describes a table reference.
        https://cloud.google.com/bigquery/docs/reference/rest/v2/TableReference
    '''

    project_id: str
    dataset_id: str
    table_id: str
