from typing import TypedDict, Dict, List, Optional

class JobReference(TypedDict):
    '''
        Describes a job reference.
        https://cloud.google.com/bigquery/docs/reference/rest/v2/JobReference
    '''

    project_id: str
    job_id: str
    location: str
