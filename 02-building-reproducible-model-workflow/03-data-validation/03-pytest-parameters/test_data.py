# -*- coding: utf-8 -*-
"""Non-deterministict tests.

Created on: 3/26/2022
@author: Heber Trujillo <heber.trj.urt@gmail.com> 
Licence,
"""
from typing import Callable
import scipy.stats


def test_kolmogorov_smirnov(
        data: Callable,
        ks_alpha: Callable
):
    """Test X's uni-variate distribution"""

    sample1, sample2 = data


    columns = [
        "danceability",
        "energy",
        "loudness",
        "speechiness",
        "acousticness",
        "instrumentalness",
        "liveness",
        "valence",
        "tempo",
        "duration_ms"
    ]

    # Bonferroni correction for multiple hypothesis testing
    # (see my blog post on this topic to see where this comes from:
    # https://towardsdatascience.com/precision-and-recall-trade-off-and-multiple-hypothesis-testing-family-wise-error-rate-vs-false-71a85057ca2b)
    alpha_prime = 1 - (1 - ks_alpha)**(1 / len(columns))

    for col in columns:

        ts, p_value = scipy.stats.ks_2samp(
            data1=sample1[col],
            data2=sample2[col],
            alternative='two-sided'
        )

        # NOTE: as always, the p-value should be interpreted as the probability of
        # obtaining a test statistic (TS) equal or more extreme that the one we got
        # by chance, when the null hypothesis is true. If this probability is not
        # large enough, this dataset should be looked at carefully, hence we fail
        assert p_value > alpha_prime, (f"H0: both samples come from a population "
                                     f"with the same distribution - rejected "
                                     f"for {col}")