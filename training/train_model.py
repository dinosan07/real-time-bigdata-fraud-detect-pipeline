import pandas as pd
import numpy as np
import joblib
from sklearn.linear_model import LogisticRegression

# -----------------------------
# Generate Synthetic Training Data
# -----------------------------
np.random.seed(42)

data_size = 10000

amounts = np.random.uniform(100, 15000, data_size)

# Fraud logic: high amount more likely fraud
labels = [1 if amount > 8000 else 0 for amount in amounts]

df = pd.DataFrame({
    "amount": amounts,
    "label": labels
})

# -----------------------------
# Train Model
# -----------------------------
X = df[["amount"]]
y = df["label"]

model = LogisticRegression()
model.fit(X, y)

# -----------------------------
# Save Model
# -----------------------------
joblib.dump(model, "../models/fraud_model.pkl")

print("Model trained and saved successfully.")

