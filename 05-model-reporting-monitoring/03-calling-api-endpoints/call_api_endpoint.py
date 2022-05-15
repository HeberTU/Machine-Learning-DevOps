# -*- coding: utf-8 -*-
"""Script to call a Flask API from CLI.

Created on: 15/5/22
@author: Heber Trujillo <heber.trj.urt@gmail.com>
Licence,
"""
import subprocess
import requests
from enum import Enum


class Endpoint(Enum):
    """Available endoint"""

    home: str = ''
    get_data_size: str = 'size'
    get_data_summary: str = 'summary'


def call_api_by_subprocess(
        endpoint: Endpoint,
        query_parms: str
) -> str:
    """Call API from CLI using subprocess module.

    Args:
        endpoint: API endpoint
        query_parms: Query parameters for API endpoint.

    Returns:
        response: API response.

    """
    response = subprocess.run(
        args=[
            'curl',
            '-X',
            'GET',
            f'127.0.0.1:8000/{endpoint}?{query_parms}'
        ],
        capture_output=True
    ).stdout

    return response


def call_apy_by_requests(
        endpoint: Endpoint,
        query_parms: str
) -> str:
    """Call API from CLI using requests module.

    Args:
        endpoint: API endpoint
        query_parms: Query parameters for API endpoint.

    Returns:
        response: API response.

    """
    return requests.get(
        url=f'http://127.0.0.1:8000/{endpoint}?{query_parms}'
    ).content


if __name__ == '__main__':

    r = call_api_by_subprocess(
        endpoint='size',
        query_parms='filename=testdata.csv'
    )

    print(r)

    r = call_apy_by_requests(
        endpoint='summary',
        query_parms='filename=testdata.csv'
    )

    print(r)