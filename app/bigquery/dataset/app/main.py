import asyncio
import requests

from fastapi import FastAPI
from google.cloud.bigquery import (
    Client,
    LoadJobConfig,
    WriteDisposition,
    SchemaUpdateOption,
)

BIGSIGHTS_PROJECT_ID = 'sandbox-athevenot'
BIGSIGHTS_DATASET_ID = 'bigsights_bigquery'
client = Client(project=BIGSIGHTS_PROJECT_ID)

app = FastAPI()

def self_url():
    return 'http://0.0.0.0:8080'

async def self_get(endpoint: str):
    response = await asyncio.to_thread(
        requests.get, url=f'{self_url()}/{endpoint}'
    )
    return response.json()


@app.get('/')
async def fetch_all():
    project_ids = ['sandbox-athevenot']

    project_async_fetch = [
        asyncio.create_task(self_get(endpoint=f'project_id/{project_id}'))
        for project_id in project_ids
    ]
    projects_results = await asyncio.gather(*project_async_fetch)

    return projects_results

@app.get('/project_id/{project_id}')
async def fetch_project(project_id: str):
    datasets = list(client.list_datasets(project=project_id))
    
    datasets_async_fetch = [
        asyncio.create_task(self_get(
            endpoint=f'project_id/{project_id}/dataset_id/{dataset.dataset_id}'
        ))
        for dataset in datasets
    ]
    datasets_results = await asyncio.gather(*datasets_async_fetch)

    return datasets_results

def table_reference(table_id: str):
    table_reference = '.'.join((
        BIGSIGHTS_PROJECT_ID,
        BIGSIGHTS_DATASET_ID,
        table_id
    ))
    return table_reference


@app.get('/project_id/{project_id}/dataset_id/{dataset_id}')
def fetch_project_dataset(project_id: str, dataset_id: str):
    dataset = client.get_dataset(dataset_ref=dataset_id)
    tables = [
        client.get_table(table=table.reference)
        for table in client.list_tables(dataset=dataset)
    ]
    
    job_config = LoadJobConfig()
    job_config.write_disposition = WriteDisposition.WRITE_APPEND
    job_config.schema_update_options = [
        SchemaUpdateOption.ALLOW_FIELD_ADDITION
    ]
    client.insert_rows_json(
        table=table_reference('d_dataset'),
        json_rows=[dataset.to_api_repr()],
        # job_config=job_config,
    )
    if tables:
        client.insert_rows_json(
            table=table_reference('d_table'),
            json_rows=[table.to_api_repr() for table in tables],
            # job_config=job_config,
        )
    return (
        f'{project_id}.{dataset_id}.{table.table_id}'
        for table in tables
    )


# if __name__ == "__main__":
#     import os
#     import uvicorn
#     uvicorn.run(app, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
