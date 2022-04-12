# -*- coding: utf-8 -*-
"""Preprocesses the fake data.

Created on: 4/12/2022
@author: Heber Trujillo <heber.trj.urt@gmail.com> 
Licence,
"""
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def main(input: str) -> None:
    """Preprocesses the fake data."""

    df = pd.read_csv("./data/fake_data.csv")

    X = df["feature"].values
    y = df["label"].values

    scaler = MinMaxScaler()
    X = scaler.fit_transform(X.reshape(-1, 1))
    print(X)

    np.savetxt("./data/X.csv", X)
    np.savetxt("./data/y.csv", y)


if __name__ == '__main__':
    main(input='')
