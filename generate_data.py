import os
os.makedirs("data", exist_ok=True)

import pandas as pd
import numpy as np

np.random.seed(42)

# USERS
users = pd.DataFrame({
    "UserId": range(1, 101),
    "ContinentId": np.random.randint(1, 5, 100),
    "RegionId": np.random.randint(1, 10, 100),
    "CountryId": np.random.randint(1, 20, 100),
    "CityId": np.random.randint(1, 50, 100)
})

# ATTRACTION TYPES
atype = pd.DataFrame({
    "AttractionTypeId": range(1, 6),
    "AttractionType": ["Beach", "Museum", "Park", "Temple", "Monument"]
})

# ATTRACTIONS
items = pd.DataFrame({
    "AttractionId": range(1, 51),
    "AttractionCityId": np.random.randint(1, 50, 50),
    "AttractionTypeId": np.random.randint(1, 6, 50),
    "Attraction": [f"Attraction_{i}" for i in range(1, 51)],
    "AttractionAddress": ["Address"] * 50
})

# VISIT MODES
visit_mode = pd.DataFrame({
    "VisitModeId": range(1, 5),
    "VisitMode": ["Business", "Family", "Couples", "Friends"]
})

# TRANSACTIONS
transactions = pd.DataFrame({
    "TransactionId": range(1, 501),
    "UserId": np.random.randint(1, 101, 500),
    "VisitYear": np.random.randint(2018, 2024, 500),
    "VisitMonth": np.random.randint(1, 13, 500),
    "VisitMode": np.random.choice(visit_mode["VisitMode"], 500),
    "AttractionId": np.random.randint(1, 51, 500),
    "Rating": np.random.randint(1, 6, 500)
})

# SAVE FILES
users.to_csv("data/User.csv", index=False)
atype.to_csv("data/Type.csv", index=False)
items.to_csv("data/Item.csv", index=False)
visit_mode.to_csv("data/VisitMode.csv", index=False)
transactions.to_csv("data/Transaction.csv", index=False)

print("CSV FILES CREATED SUCCESSFULLY")
