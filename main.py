import os
import pandas as pd
import logging

from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

import numpy as np

LOG = logging.getLogger()


def test_function():
    print("TEST DUMP 3")
    print(os.listdir())

def trigger():
    LOG.info("shape of data is : {}")
    data = make_classification(n_samples=10000,n_features=5,n_classes=2)
    data = pd.DataFrame(np.column_stack(data))
    LOG.info(f"shape of data is : {data.shape}")
    data.columns =["a","b","c","d","e","target"]
    model  = RandomForestClassifier()
    model.fit(data.drop("target",axis=1),data["target"])

    pred = model.predict(data.drop("target",axis=1))

    acc = accuracy_score(data["target"],pred)

    print(acc)
    LOG.info(f"ACCURACY : {acc} ")



