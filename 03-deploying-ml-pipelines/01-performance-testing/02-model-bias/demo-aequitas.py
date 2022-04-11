# -*- coding: utf-8 -*-
"""Running Aequitas to investigate the potential bias in a model/data set.

Created on: 4/9/2022
@author: Heber Trujillo <heber.trj.urt@gmail.com> 
Licence,
"""
from typing import Tuple
from aequitas.plotting import Plot

import pandas as pd

from aequitas.group import Group
from aequitas.bias import Bias
from aequitas.fairness import Fairness

from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import \
    OneHotEncoder,\
    label_binarize,\
    LabelEncoder, LabelBinarizer

from sklearn.compose import TransformedTargetRegressor
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 10)


def read_car_data(pth: str = "./data/car.csv") -> pd.DataFrame:
    return pd.read_csv(pth)


def preprocess_car_data(
        df: pd.DataFrame
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """

    Args:
        df: cars data frame

    Returns:
        X: features
        y: target variable
    """

    df = df.where(df != 'good', 'acc')
    df = df.where(df != 'vgood', 'acc')

    y = df.pop('car')
    X = df

    y = label_binarize(y.values, classes=['unacc', 'acc']).ravel()

    return X, y


def build_model():
    """Create a simple regression pipeline"""

    model = Pipeline(
        steps=[
            ('one', OneHotEncoder(handle_unknown="ignore", sparse=False)),
            ('lr', LogisticRegression(max_iter=1000))
        ]
    )

    return model


if __name__ == '__main__':

    ap = Plot()

    X, y = preprocess_car_data(
        df=read_car_data()
    )

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25,
                                                        random_state=23)

    model = build_model()
    model.fit(X_train, y_train)

    scores = model.predict_proba(X_test)
    pred = model.predict(X_test)

    f1 = f1_score(y_test, pred)
    print(f"F1 score: {f1:.4f}")

    df_aq = X_test.copy()
    df_aq['label_value'] = y_test
    df_aq['score'] = pred

    group = Group()
    xtab, idxs = group.get_crosstabs(df_aq)
    xtab.head()

    bias = Bias()
    bias_df = bias.get_disparity_major_group(xtab, original_df=df_aq, alpha=0.05,
                                             mask_significance=True)
    bias_df.head()