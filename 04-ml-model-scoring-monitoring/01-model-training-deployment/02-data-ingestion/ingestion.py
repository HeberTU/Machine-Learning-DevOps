# -*- coding: utf-8 -*-
"""Python demo script for data ingestion.

Created on: 4/30/2022
@author: Heber Trujillo <heber.trj.urt@gmail.com>
Licence,
"""
import os
from pathlib import Path
from typing import List
import glob
import pandas as pd
import pandera as pa
from pandera.typing import DataFrame, Series


class InputSchema(pa.SchemaModel):
    col1: Series[int] = pa.Field(coerce=True)
    col2: Series[int] = pa.Field(coerce=True)
    col3: Series[int] = pa.Field(coerce=True, isin=[0, 1])


def get_all_files(path: Path) -> List[Path]:
    """Read all csv file within path directory tree.

    Args:
        path: path from which the recursive reading will start.

    Returns:
        file_paths: List of absolute file paths.

    """
    file_paths = []
    for root, dirs, files in os.walk(path):
        files = glob.glob(os.path.join(root, '*.csv'))
        for f in files:
            file_paths.append(os.path.abspath(f))

    return file_paths


def merge_files(
        file_paths: List[Path]
) -> DataFrame[InputSchema]:
    """Merge all files from a list of directories.

    Args:
        file_paths: List of absolute file paths.

    Returns:
        result: Dataframe containing all files.

    """
    result = pd.DataFrame()

    @pa.check_types
    def validate_data(
            df: DataFrame[InputSchema]) -> DataFrame[InputSchema]:
        return df

    for file_path in file_paths:

        df = validate_data(
            df=pd.read_csv(file_path)
        )

        result = pd.concat(
            objs=[result, df]
        )

    return result.drop_duplicates()


def main(path: Path) -> None:
    """Main function"""

    file_paths = get_all_files(path=path)

    result = merge_files(file_paths=file_paths)

    result.to_csv(
        path_or_buf=path / "result.csv",
        index=False
    )


if __name__ == '__main__':

    ROOT_PATH = Path(__file__).resolve().parents[0]
    main(ROOT_PATH)
