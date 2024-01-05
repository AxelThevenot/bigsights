from enum import Enum
from typing import TypedDict, Dict, List, Optional, Self


class TypeKind(Enum):
    ''''
    Describes the kind of the datatype.
    https://cloud.google.com/bigquery/docs/reference/rest/v2/StandardSqlDataType#typekind
    '''

    TYPE_KIND_UNSPECIFIED = 'TYPE_KIND_UNSPECIFIED'
    INT64 = 'INT64'
    BOOL = 'BOOL'
    FLOAT64 = 'FLOAT64'
    STRING = 'STRING'
    BYTES = 'BYTES'
    TIMESTAMP = 'TIMESTAMP'
    DATE = 'DATE'
    TIME = 'TIME'
    DATETIME = 'DATETIME'
    GEOGRAPHY = 'GEOGRAPHY'
    NUMERIC = 'NUMERIC'
    BIGNUMERIC = 'BIGNUMERIC'
    JSON = 'JSON'
    ARRAY = 'ARRAY'
    STRUCT = 'STRUCT'
    
class StandardSqlStructType(TypedDict):
    '''
        Describes a SQL STRUCT type.
        https://cloud.google.com/bigquery/docs/reference/rest/v2/StandardSqlDataType#standardsqlstructtype
    '''

    fields: 'StandardSqlDataType'


class StandardSqlDataType(TypedDict):
    '''
        Describes a SQL type.
        https://cloud.google.com/bigquery/docs/reference/rest/v2/StandardSqlDataType
    '''

    type_kind: TypeKind
    array_element_type: Self
    struct_type: StandardSqlStructType
