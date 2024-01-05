from enum import Enum
from typing import TypedDict, Dict, List, Optional, Literal

from .dataset import DatasetReference
from .table import TimePartitioning, RangePartitioning, Clustering, ErrorProto
from .table_reference import TableReference
from .query_parameter import QueryParameter
from .encryption_configuration import EncryptionConfiguration
from .connection_property import ConnectionProperty
from .standard_sql_data_type import StandardSqlDataType
from .job_reference import JobReference


class KeyResultStatementKind(Enum):
    '''
        Describes how the key result is determined.
        https://cloud.google.com/bigquery/docs/reference/rest/v2/Job#keyresultstatementkind
    '''

    KEY_RESULT_STATEMENT_KIND_UNSPECIFIED = 'KEY_RESULT_STATEMENT_KIND_UNSPECIFIED'
    LAST = 'LAST'
    FIRST_SELECT = 'FIRST_SELECT'


class SystemVariables(TypedDict):
    '''
        Describes system variables given to a query..
        https://cloud.google.com/bigquery/docs/reference/rest/v2/Job#JobConfigurationQuery
    '''

    types: Dict[str, StandardSqlDataType]
    values: Dict


class ScriptOptions(TypedDict):
    '''
        Describes options related to script execution.
        https://cloud.google.com/bigquery/docs/reference/rest/v2/Job#ScriptOptions
    '''

    statement_timeout_ms: str
    statement_byte_budget: str
    key_result_statement: KeyResultStatementKind


class JobStatistics(TypedDict):
    '''
        Represents statistics for a job.
        https://cloud.google.com/bigquery/docs/reference/rest/v2/Job#JobStatistics
    '''

    creation_time: str
    start_time: str
    end_time: str
    total_bytes_processed: str
    completion_ratio: float
    quota_deferments: List[str]
    query: 'JobStatistics2'  # type: ignore
    load: 'JobStatistics3'  # type: ignore
    extract: 'JobStatistics4'  # type: ignore
    total_slot_ms: str
    reservation_usage: List[Dict[str, str]]
    reservation_id: str
    num_child_jobs: str
    parent_job_id: str
    script_statistics: 'ScriptStatistics'  # type: ignore
    row_level_security_statistics: 'RowLevelSecurityStatistics'  # type: ignore
    data_masking_statistics: 'DataMaskingStatistics'  # type: ignore
    transaction_info: 'TransactionInfo'  # type: ignore
    session_info: 'SessionInfo'  # type: ignore
    final_execution_duration_ms: str

class JobConfigurationQuery(TypedDict):
    '''
        Configures a query job.
        https://cloud.google.com/bigquery/docs/reference/rest/v2/Job#JobConfigurationQuery
    '''

    query: str
    destination_table: TableReference
    table_definitions: Dict[str, 'ExternalDataConfiguration']  # type: ignore
    user_defined_function_resources: List['UserDefinedFunctionResource']  # type: ignore
    create_disposition: str
    write_disposition: str
    default_dataset: DatasetReference
    priority: str
    # preserve_nulls: bool [deprecated]
    allow_large_results: bool
    use_query_cache: bool
    flatten_results: bool
    # maximum_billing_tier: int [deprecated]
    maximum_bytes_billed: str
    use_legacy_sql: bool
    parameter_mode: str
    query_parameters: List[QueryParameter]
    schema_update_options: List[str]
    time_partitioning: TimePartitioning
    range_partitioning: RangePartitioning
    clustering: Clustering
    destination_encryption_configuration: EncryptionConfiguration
    script_options: ScriptOptions
    connection_properties: List[ConnectionProperty]
    create_session: bool
    system_variables: SystemVariables


class JobConfiguration(TypedDict):
    '''
        Describes the job configuration.
        https://cloud.google.com/bigquery/docs/reference/rest/v2/Job#JobConfiguration
    '''

    job_type: str
    query: JobConfigurationQuery
    load: 'JobConfigurationLoad'  # type: ignore
    copy: 'JobConfigurationTableCopy'  # type: ignore
    dry_run: bool
    job_timeout_ms: str
    labels: Dict[str, str]


class JobStatus(TypedDict):
    '''
        Describes the status of a job.
        https://cloud.google.com/bigquery/docs/reference/rest/v2/Job#JobStatus
    '''

    error_result: ErrorProto
    errors: List[ErrorProto]
    state: Literal['PENDING', 'RUNNING', 'DONE']


class Job(TypedDict):
    '''
        Describes the BigQuery job.
        https://cloud.google.com/bigquery/docs/reference/rest/v2/Job
    '''

    kind: str  # must be 'bigquery#job' ?
    etag: str
    id: str
    self_link: str
    user_email: str
    configuration: JobConfiguration
    job_reference: JobReference
    statistics: 'JobStatistics'  # type: ignore
    status: JobStatus
    principal_subject: Optional[str]  # re-read the doc 
