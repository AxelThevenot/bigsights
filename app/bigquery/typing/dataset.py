from typing import TypedDict, Dict, List, Optional

class DatasetReference(TypedDict):
    '''
        Describes a dataset.
        https://cloud.google.com/bigquery/docs/reference/rest/v2/datasets#DatasetReference
    '''

    project_id: Optional[str]
    dataset_id: str
