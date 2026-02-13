# ==============================
# Module 4 — Classification Model
# ==============================

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# -----------------------------
# Load dataset
# -----------------------------
df = pd.read_csv("data/final_dataset.csv")

# -----------------------------
# Prepare Features
# -----------------------------
X = df.drop(columns=["Rating", "RatingCategory", "Attraction", "AttractionAddress"])
y = df["RatingCategory"]

# Encode target labels
le = LabelEncoder()
y = le.fit_transform(y)

# Convert categorical features
X = pd.get_dummies(X, drop_first=True)

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------
# Train Model
# -----------------------------
clf = RandomForestClassifier(random_state=42)
clf.fit(X_train, y_train)

# Predictions
y_pred = clf.predict(X_test)

# -----------------------------
# Evaluation
# -----------------------------
accuracy = accuracy_score(y_test, y_pred)

print("\nClassification Results")
print("-----------------------")
print("Accuracy:", round(accuracy, 4))
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))
 