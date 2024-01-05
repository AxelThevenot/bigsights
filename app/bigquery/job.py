from typing import Optional, Iterable
from datetime import datetime
from google.cloud.bigquery import (
    Client,
    QueryJob,
)


from .typing.job import Job

project_id = 'sandbox-athevenot'
client = Client(project_id)

def get_child_jobs(job: QueryJob) -> Iterable[QueryJob]:

    if job.num_child_jobs:
        job_iterator = client.list_jobs(
            project=job.project,
            parent_job=job.job_id
        )
        for job in job_iterator:
            yield from get_child_jobs(job=job)
    else:
        yield job

def get_job_iterator(
        project_id: str,
        min_creation_time: Optional[datetime] = datetime.fromisoformat('2024-01-04'),
        max_creation_time: Optional[datetime] = None,
        state_filter: str = 'done',
    ) -> Iterable[QueryJob]:

    job_iterator = client.list_jobs(
        project=project_id,
        max_results=4,
        page_token=None,
        all_users=True,
        state_filter=state_filter,
        min_creation_time=min_creation_time,
        max_creation_time=max_creation_time,
    )
    return job_iterator



for job in get_job_iterator(project_id=project_id):

    print(job.job_id, job.num_child_jobs, job.query.replace('\n', ' '))  # type: ignore

    for child_job in get_child_jobs(job):
        print(job.job_id, child_job.num_child_jobs, child_job.query.replace('\n', ' ')) # type: ignore
