# ==============================
# Module 5 — Advanced Recommendation System
# ==============================

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# -----------------------------
# Load dataset
# -----------------------------
df = pd.read_csv("data/final_dataset.csv")

# -----------------------------
# Create User-Item Matrix
# -----------------------------
user_item_matrix = df.pivot_table(
    index="UserId",
    columns="AttractionId",
    values="Rating"
).fillna(0)

print("User-Item Matrix Shape:", user_item_matrix.shape)

# -----------------------------
# Compute User Similarity
# -----------------------------
user_similarity = cosine_similarity(user_item_matrix)

similarity_df = pd.DataFrame(
    user_similarity,
    index=user_item_matrix.index,
    columns=user_item_matrix.index
)

print("Similarity Matrix Shape:", similarity_df.shape)

# -----------------------------
# Improved Recommendation Function
# -----------------------------
def recommend_attractions(user_id, top_n=5):

    # Similar users (excluding self)
    similar_users = similarity_df[user_id].sort_values(ascending=False)[1:6]

    # Weighted ratings
    weighted_scores = pd.Series(0, index=user_item_matrix.columns)

    for sim_user, sim_score in similar_users.items():
        weighted_scores += user_item_matrix.loc[sim_user] * sim_score

    # Remove already visited attractions
    visited = user_item_matrix.loc[user_id]
    weighted_scores = weighted_scores[visited == 0]

    # Get top recommendations
    top_attractions = weighted_scores.sort_values(ascending=False).head(top_n)

    # Map AttractionId to Attraction Name
    attraction_names = df[["AttractionId", "Attraction"]].drop_duplicates()
    top_attractions = top_attractions.reset_index()
    top_attractions.columns = ["AttractionId", "Score"]

    result = top_attractions.merge(attraction_names, on="AttractionId")

    return result[["Attraction", "Score"]]

# -----------------------------
# Example
# -----------------------------
user_id_example = 1
recommendations = recommend_attractions(user_id_example)

print("\nTop Smart Recommendations for User 1:")
print(recommendations)
