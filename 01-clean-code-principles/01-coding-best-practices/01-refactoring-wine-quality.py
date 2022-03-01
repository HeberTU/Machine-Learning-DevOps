# -*- coding: utf-8 -*-
"""
In this exercise, we'll refactor code that analyzes a wine quality dataset
taken from the UCI Machine Learning Repository here. Each row contains data
on a wine sample, including several physicochemical properties gathered from
tests, as well as a quality rating evaluated by wine experts.

Created on: 01/03/2022
@author: Heber Trujillo <heber.trj.urt@gmail.com>
Licence,
"""
import pandas as pd

df = pd.read_csv('./data/winequality-red.csv', sep=';')
df.head()

# Renaming Columns
# Wrong
new_df = df.rename(columns={'fixed acidity': 'fixed_acidity',
                            'volatile acidity': 'volatile_acidity',
                            'citric acid': 'citric_acid',
                            'residual sugar': 'residual_sugar',
                            'free sulfur dioxide': 'free_sulfur_dioxide',
                            'total sulfur dioxide': 'total_sulfur_dioxide'
                            })
new_df.head()

# Good
df.columns = [col.replace(" ", "_") for col in df.columns]
df.head()


# Analyzing Features
def numeric_to_buckets(
        df: pd.DataFrame,
        column: str
) -> None:

    meadian = df[column].median()
    df[column] = df[column]. \
        apply(
        lambda x: 'high' if x >= meadian else 'low')


for column in df.columns[:-1]:
    numeric_to_buckets(
        df=df,
        column=column
    )
    print(
        df.groupby(by=column).agg(quality=('quality', 'mean'))
    )
