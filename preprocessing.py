# ==============================
# Module 2 — Data Loading & Merging
# ==============================

import pandas as pd

# Load CSV files
users = pd.read_csv("data/User.csv")
atype = pd.read_csv("data/Type.csv")
items = pd.read_csv("data/Item.csv")
visit_mode = pd.read_csv("data/VisitMode.csv")
transactions = pd.read_csv("data/Transaction.csv")

# Merge datasets step by step

# Merge transactions with users
df = transactions.merge(users, on="UserId", how="left")

# Merge with items
df = df.merge(items, on="AttractionId", how="left")

# Merge with attraction types
df = df.merge(atype, on="AttractionTypeId", how="left")

# Create RatingCategory for classification
df["RatingCategory"] = pd.cut(
    df["Rating"],
    bins=[0, 2, 4, 5],
    labels=["Negative", "Neutral", "Positive"]
)

print("Preprocessing completed successfully.")
print("Final dataset shape:", df.shape)

# Export merged file (optional)
df.to_csv("data/final_dataset.csv", index=False)
