# ==============================
# Module 3 — Regression Model
# ==============================

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error

# -----------------------------
# Load dataset
# -----------------------------
df = pd.read_csv("data/final_dataset.csv")

# -----------------------------
# Feature Selection
# -----------------------------
# DROP the target column "Rating" to avoid data leakage
X = df.drop(columns=["Rating", "RatingCategory", "Attraction", "AttractionAddress"])
y = df["Rating"]

# Convert categorical variables into numeric
X = pd.get_dummies(X, drop_first=True)

# -----------------------------
# Train-Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------
# Linear Regression
# -----------------------------
lr = LinearRegression()
lr.fit(X_train, y_train)

y_pred_lr = lr.predict(X_test)

r2_lr = r2_score(y_test, y_pred_lr)
rmse_lr = np.sqrt(mean_squared_error(y_test, y_pred_lr))

# -----------------------------
# Random Forest Regressor
# -----------------------------
rf = RandomForestRegressor(random_state=42)
rf.fit(X_train, y_train)

y_pred_rf = rf.predict(X_test)

r2_rf = r2_score(y_test, y_pred_rf)
rmse_rf = np.sqrt(mean_squared_error(y_test, y_pred_rf))

# -----------------------------
# Print Results
# -----------------------------
print("\nRegression Results")
print("-------------------")
print("Linear Regression R2:", round(r2_lr, 4))
print("Linear Regression RMSE:", round(rmse_lr, 4))
print()
print("Random Forest R2:", round(r2_rf, 4))
print("Random Forest RMSE:", round(rmse_rf, 4))
