from sklearn.ensemble import IsolationForest
import numpy as np
import json

# Load normal logs
with open("normal_logs.json", "r") as f:
    normal_logs = json.load(f)

# Convert to array of features
X_train = [[log["metric"], log["error_rate"], log["latency"]] for log in normal_logs]

clf = IsolationForest()
clf.fit(X_train)
model = clf
