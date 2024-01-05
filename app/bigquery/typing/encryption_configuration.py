from typing import TypedDict, Dict, List, Optional

class EncryptionConfiguration(TypedDict):
    '''
        Describes a custom encryption configuration.
        https://cloud.google.com/bigquery/docs/reference/rest/v2/EncryptionConfiguration
    '''

    kms_key_name: str
