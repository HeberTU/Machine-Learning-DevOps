# -*- coding: utf-8 -*-
"""Trains a logistic regression.

Created on: 4/12/2022
@author: Heber Trujillo <heber.trj.urt@gmail.com> 
Licence,
"""
import numpy as np
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
import yaml

params = yaml.safe_load(open("params.yaml"))["train"]

X = np.loadtxt("./data/X.csv")
y = np.loadtxt("./data/y.csv")

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=params["test_size"],
    random_state=params["random_state"],
)

lr = LogisticRegression(C=params["C"])
lr.fit(X_train.reshape(-1, 1), y_train)

preds = lr.predict(X_test.reshape(-1, 1))
f1 = f1_score(y_test, preds)
print(f"F1 score: {f1:.4f}")

pickle.dump(lr, open("./models/model.pkl", "wb"))