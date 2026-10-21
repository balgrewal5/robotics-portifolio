
"""
Robotics Roadmap 1 - Week 21
Machine Learning: Sensor Anomaly Detection

Isolation Forest for detecting abnormal motor behaviour.
Features: RPM, current (A), vibration.
Uses synthetic sensor data and median imputation.
"""

import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score, precision_score, recall_score

rng = np.random.default_rng(42)


def samples(count, mean, spread):
    """Generate simulated sensor readings."""
    return rng.normal(mean, spread, size=(count, 3))


# Normal motor operating conditions
normal_mean = [20.0, 0.40, 0.20]
normal_std = [1.0, 0.05, 0.04]

# Training data: 1,000 normal readings with 2% missing values
train = samples(1000, normal_mean, normal_std)
train[rng.random(train.shape) < 0.02] = np.nan

# Independent validation and test samples
validation = samples(300, normal_mean, normal_std)
normal_test = samples(300, normal_mean, normal_std)

# Simulated motor faults
faults = {
    "overload": samples(100, [16, 0.62, 0.28], [1, 0.06, 0.04]),
    "imbalance": samples(100, [20, 0.44, 0.35], [1, 0.05, 0.04]),
    "stall": samples(100, [2, 1.0, 0.24], [0.7, 0.1, 0.04]),
}

# Replace missing values using training-set medians
imputer = SimpleImputer(strategy="median")
X_train = imputer.fit_transform(train)

# Train unsupervised anomaly detector
model = IsolationForest(
    n_estimators=100,
    contamination=0.05,
    random_state=42
)
model.fit(X_train)

# Test using normal and faulty readings
X_test = np.vstack([normal_test, *faults.values()])
y_test = np.array([0] * 300 + [1] * 300)

scores = model.decision_function(imputer.transform(X_test))
validation_scores = model.decision_function(
    imputer.transform(validation)
)

# Compare default and adjusted anomaly thresholds
thresholds = {
    "Default": 0.0,
    "Adjusted": np.quantile(validation_scores, 0.10)
}

for name, threshold in thresholds.items():
    predictions = (scores < threshold).astype(int)

    print(f"\n{name} threshold: {threshold:.3f}")
    print(f"Accuracy: {accuracy_score(y_test, predictions):.1%}")
    print(f"Precision: {precision_score(y_test, predictions):.1%}")
    print(f"Recall: {recall_score(y_test, predictions):.1%}")
    print(f"False alarms: {int(predictions[:300].sum())}")

    for index, fault in enumerate(faults):
        start = 300 + index * 100
        detected = predictions[start:start + 100].mean()
        print(f"{fault} detection: {detected:.1%}")
