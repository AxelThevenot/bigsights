from typing import TypedDict, Dict, List, Optional, Self


class QueryParameterType(TypedDict):
    '''
        Describes a type of a parameter given to a query.
        https://cloud.google.com/bigquery/docs/reference/rest/v2/QueryParameter#queryparametertype
    '''

    type: str
    array_type: Optional[Self]
    struct_types: Optional[List[Self]]
    description: Optional[str]

class QueryParameterValue(TypedDict):
    '''
        Describes a value of a parameter given to a query.
        https://cloud.google.com/bigquery/docs/reference/rest/v2/QueryParameter#queryparametervalue
    '''

    value: Optional[str]
    array_values: Optional[List[Self]]
    struct_values: Optional[Dict[str, Self]]

class QueryParameter(TypedDict):
    '''
        Describes a parameter given to a query.
        https://cloud.google.com/bigquery/docs/reference/rest/v2/QueryParameter
    '''

    name: Optional[str]
    parameter_type: QueryParameterType
    parameter_value: QueryParameterValue
