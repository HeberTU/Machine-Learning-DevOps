# -*- coding: utf-8 -*-
"""Model drift measure demo.

Created on: 7/5/22
@author: Heber Trujillo <heber.trj.urt@gmail.com>
Licence,
"""
import ast
from typing import Optional, List
from pathlib import Path
import numpy as np


def read_previous_scores(path: Path) -> List[float]:
    """Read previous score from a text file.

    Args:
        path: path from which the previous scores are read.

    Returns:
        scores: List of previous scores.

    """
    with open(path / "previousscores.txt") as file:
        scores = file.readlines()

    return ast.literal_eval(scores[0])


def raw_comparison_test(
        scores: List[float],
        new_score: float
) -> bool:
    """Check model drift by raw comparison.

    Args:
        scores: List of previous scores.
        new_score: New score to be tested.

    Returns:
        result: True if the new score is worse than all previous
         scores.

    """
    result = [new_score < x for x in scores]

    return all(result)


def parametric_significance_test(
        scores: List[float],
        new_score: float
) -> bool:
    """Check model drift by parametric comparison.

    Args:
        scores: List of previous scores.
        new_score: New score to be tested.

    Returns:
        result: True if the new_score is significantly lower than
          previous observations.

    """
    scores = np.array(scores)

    mean = scores.mean()

    std = scores.std()

    return new_score < mean - 2 * std


def non_parametric_outlier_test(
        scores: List[float],
        new_score: float
) -> bool:
    """Check model drift by non-parametric outlier comparison.

    Args:
        scores: List of previous scores.
        new_score: New score to be tested.

    Returns:
        result: True if the new_score is significantly lower than
          previous observations.

    """

    q25, q75 = np.percentile(a=scores, q=[25, 75])

    iqr = q75 - q25

    return new_score < q25 - 1.5 * iqr


if __name__ == '__main__':

    NEWR2 = 0.3625

    ROOT_PATH = Path(__file__).resolve().parents[0]

    r2_scores = read_previous_scores(path=ROOT_PATH)

    raw_comparison = raw_comparison_test(
        scores=r2_scores,
        new_score=NEWR2
    )

    print(f"Raw comparison test: {raw_comparison}")

    parametric_comparison = parametric_significance_test(
        scores=r2_scores,
        new_score=NEWR2
    )

    print(f"Parametric comparison test: {parametric_comparison}")

    non_parametric_comparison = non_parametric_outlier_test(
        scores=r2_scores,
        new_score=NEWR2
    )

    print(f"Non-parametric comparison test: {non_parametric_comparison}")
