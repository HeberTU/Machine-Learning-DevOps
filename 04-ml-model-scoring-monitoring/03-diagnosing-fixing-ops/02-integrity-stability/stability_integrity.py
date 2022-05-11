# -*- coding: utf-8 -*-
"""Integrity and Stability demo script.

Created on: 11/5/22
@author: Heber Trujillo <heber.trj.urt@gmail.com>
Licence,
"""
import ast
from typing import List, Dict
from pathlib import Path
import pandas as pd
import pandera as pa
from pandera.typing import DataFrame, Series


class InputSchema(pa.SchemaModel):
    """Data input schema."""
    col1: Series[float] = pa.Field(nullable=True, coerce=True)
    col2: Series[float] = pa.Field(nullable=True, coerce=True)
    col3: Series[int] = pa.Field(coerce=True, isin=[0, 1])


def read_test_data(path: Path) -> DataFrame[InputSchema]:
    """Read the test data for model scoring.

    Args:
        path: path from which the data will be imported.

    Returns:
        test_data: Test data.

    """
    test_data = pd.read_csv(path / "samplefile2.csv")

    @pa.check_types
    def validate_data(
            df: DataFrame[InputSchema]) -> DataFrame[InputSchema]:
        return df

    return validate_data(test_data)


def get_historic_means(path: Path) -> List[float]:
    """Read historic means.

    Args:
        path: Path from which the historic data will be read.

    Returns:
        historic_means: Historic means.

    """

    with open(file=path / "historicmeans.txt", mode='r') as file:
        historic_means = file.readlines()

    return ast.literal_eval(historic_means[0])


def check_data_integrity(df: DataFrame[InputSchema]) -> pd.Series:
    """Test data integrity.

    Args:
        df: Input data

    Returns:
        integrity_check: Percentage of NaNs by column.

    """
    return df.isna().sum() / df.shape[0]


def check_data_stability(
        df: DataFrame[InputSchema],
        historic_means: List[float]
) -> Dict[str, float]:
    """Test data stability.

    Args:
        df: Input data
        historic_means: Historic means.

    Returns:
        results: mean comparison for each column.

    """
    results = {}
    i = 0
    for col, row in pd.DataFrame(df.mean()).iterrows():
        results[col] = (row[0] - historic_means[i]) / historic_means[i]
        i += 1

    return results


if __name__ == '__main__':

    ROOT_PATH = Path(__file__).resolve().parents[0]

    means = get_historic_means(path=ROOT_PATH)

    new_data = read_test_data(path=ROOT_PATH)

    print("Data Integrity check:")
    print(check_data_integrity(df=new_data))

    print("Data Stability check:")
    print(check_data_stability(df=new_data, historic_means=means))
