# -*- coding: utf-8 -*-
"""Data Slicing

Created on: 4/8/2022
@author: Heber Trujillo <heber.trj.urt@gmail.com> 
Licence,
"""
import pandas as pd
from sklearn import datasets


def data() -> pd.DataFrame:
    """Load the iris data set."""
    iris = datasets.load_iris()
    df = pd.concat(
        objs=[
            pd.DataFrame(
                data=iris.data,
                columns=iris.feature_names
            ),
            pd.DataFrame(
                data=iris.target,
                columns=['category']
            )
        ],
        axis=1
    )

    return df


def calculate_column_stats(
        df: pd.DataFrame,
        num_feature: str,
        cat_feature: str
) -> pd.DataFrame:
    """Outputs the descriptive stats for a numerical feature
     while the categorical variable is held fixed.

    Args:
        df: pandas dataframe
        num_feature: numerical feature
        cat_feature: categorical feature

    Returns:

    """
    stats = df.\
        groupby(
            by=cat_feature)\
        [num_feature].\
        describe().\
        reset_index()

    return stats


if __name__ == '__main__':

    iris_df = data()
    numerical_features = iris_df.columns[:-1]
    cat_col = iris_df.columns[-1]

    for column in numerical_features:

        stats = calculate_column_stats(
            df=iris_df,
            num_feature=column,
            cat_feature=cat_col
        )

        print(f"Stats for {column}: ")
        print(stats)

