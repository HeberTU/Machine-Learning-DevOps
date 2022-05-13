# -*- coding: utf-8 -*-
"""API with multiple endpoints demo script.

Examples:
    Calling API Endpoints::
        $ curl -X GET "127.0.0.1:8000/summary?filename=testdata.csv"
        $ curl -X GET "127.0.0.1:8000/size?filename=testdata.csv"

Created on: 13/5/22
@author: Heber Trujillo <heber.trj.urt@gmail.com>
Licence,
"""
from pathlib import Path
from flask import Flask, request
import pandas as pd
import pandera as pa
from pandera.typing import DataFrame, Series

app = Flask(__name__)


class InputSchema(pa.SchemaModel):
    """Data input schema."""
    col1: Series[float] = pa.Field(nullable=True, coerce=True)
    col2: Series[float] = pa.Field(nullable=True, coerce=True)
    col3: Series[int] = pa.Field(coerce=True, isin=[0, 1])


def read_data(filename: str, path: Path)->DataFrame[InputSchema]:
    """Read the test data for model scoring.

    Args:
        filename: file name.
        path: Path to file.

    Returns:
        test_data: Test data.

    """
    test_data = pd.read_csv(path / filename)

    @pa.check_types
    def validate_data(
            df: DataFrame[InputSchema]) -> DataFrame[InputSchema]:
        return df

    return validate_data(test_data)


@app.route('/')
def index() -> str:
    """Says hello to user.

    Returns:
        Greeting.

    """
    user = request.args.get('user')

    return 'Hello ' + user + '\n'


@app.route('/size')
def get_data_size() -> str:
    """Calculate data frame size.

    Returns:
        size: Data frame size

    """
    filename = request.args.get('filename')
    data = read_data(filename, ROOT_PATH)
    return str(data.shape) + '\n'


@app.route('/summary')
def get_data_summary() -> str:
    """Calculate data frame summary.

    Returns:
        size: Data frame size

    """
    filename = request.args.get('filename')
    data = read_data(filename, ROOT_PATH)
    return str(data.describe()) + '\n'


if __name__ == '__main__':

    ROOT_PATH = Path(__file__).resolve().parents[0]

    app.run(host="0.0.0.0", port=8000)
