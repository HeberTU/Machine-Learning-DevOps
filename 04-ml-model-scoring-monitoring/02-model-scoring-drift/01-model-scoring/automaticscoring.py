# -*- coding: utf-8 -*-
"""Python demo script for model scoring.

Created on: 5/04/2022
@author: Heber Trujillo <heber.trj.urt@gmail.com>
Licence,
"""
import pickle
from pathlib import Path
import pandas as pd
import pandera as pa
from pandera.typing import DataFrame, Series
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score


class InputSchema(pa.SchemaModel):
    """Test data input schema."""
    col1: Series[int] = pa.Field(coerce=True)
    col2: Series[int] = pa.Field(coerce=True)
    col3: Series[int] = pa.Field(coerce=True, isin=[0, 1])


def read_test_data(path: Path) -> DataFrame[InputSchema]:
    """Read the test data for model scoring.

    Args:
        path: path from which the data will be imported.

    Returns:
        test_data: Test data.

    """
    test_data = pd.read_csv(path / "testdata.csv")

    @pa.check_types
    def validate_data(
            df: DataFrame[InputSchema]) -> DataFrame[InputSchema]:
        return df

    return validate_data(test_data)


def read_model(path: Path) -> LogisticRegression:
    """Read machen learning model.

    Args:
        path: path from which the data will be imported.

    Returns:
        model: Logistic regression model.

    """

    return pickle.load(open(path / "samplemodel.pkl", "rb"))


def score_model(
        test_data: DataFrame[InputSchema],
        model: LogisticRegression
) -> float:
    """Calculate the F1 score.

    Args:
        test_data: Test data.
        model: Logistic regression model.

    Returns:
        score: F1 score.

    """

    X = test_data.copy()
    y = X.pop("col3")

    pred = model.predict(X)

    return f1_score(y_true=y, y_pred=pred)


if __name__ == '__main__':

    ROOT_PATH = Path(__file__).resolve().parents[0]

    test_set = read_test_data(path=ROOT_PATH)

    logistic_model = read_model(path=ROOT_PATH)

    score = score_model(
        test_data=test_set,
        model=logistic_model
    )

    print(score)
