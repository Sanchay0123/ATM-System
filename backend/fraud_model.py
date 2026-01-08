import numpy as np
from sklearn.ensemble import IsolationForest

model = IsolationForest(contamination=0.1)

def train():
    data = np.array([[500],[1000],[1500],[2000],[2500]])
    model.fit(data)

def is_fraud(amount):
    return model.predict([[amount]])[0] == -1
