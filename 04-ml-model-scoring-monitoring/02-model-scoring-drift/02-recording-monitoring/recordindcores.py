# -*- coding: utf-8 -*-
""" This script shows how to record scores for ml model.

Created on: 6/5/22
@author: Heber Trujillo <heber.trj.urt@gmail.com>
Licence,
"""
from typing import Optional
from pathlib import Path
import pandas as pd
import pandera as pa
from pandera.typing import DataFrame, Series


class Scores(pa.SchemaModel):
    """Score data model"""
    metric: Series[str] = pa.Field(coerce=True, isin=["r2", "sse"])
    version: Series[int] = pa.Field(coerce=True)
    score: Series[float] = pa.Field(coerce=True)


@pa.check_types
def validate_scores(df: DataFrame[Scores]) -> DataFrame[Scores]:
    return df


def read_previous_scores(path: Path) -> DataFrame[Scores]:
    """

    Args:
        path: path from which the previous scores are read.

    Returns:
        scores: DataFrame with old scores.

    """

    return validate_scores(pd.read_csv(path / "previousscores.csv"))


def append_scores(
        df: DataFrame[Scores],
        r2_score: float,
        sse_score: float
) -> Optional[DataFrame[Scores]]:
    """Append R2 & SSE scores if SSE < all previous SSEs.

    Args:
        df: DataFrame with old scores.
        r2_score: r2 score
        sse_score: sse score

    Returns:
        None | df: DataFrame with new scores.

    """

    new_scores = DataFrame[Scores](
        {
            "metric": ["r2", "sse"],
            "version": [df.version.max() + 1] * 2,
            "score": [r2_score, sse_score]
        }
    )

    if all(sse_score < df.query("metric == 'sse'").score):

        return pd.concat(objs=[df, new_scores])

    return None


if __name__ == '__main__':

    ROOT_PATH = Path(__file__).resolve().parents[0]

    scores = read_previous_scores(path=ROOT_PATH)

    scores = append_scores(
        df=scores,
        r2_score=0.6,
        sse_score=52938
    )

    if scores is not None:
        scores.to_csv(ROOT_PATH / "previousscores.csv", index=False)
