Project title - 🌍 Tourism Experience Analytics
Classification, Prediction and Recommendation System

  🌍 Tourism Experience Analytics

An end-to-end Machine Learning pipeline for analyzing and predicting tourism experiences.  
This project implements Regression, Classification, and a User-Based Collaborative Filtering Recommendation System to extract insights from tourism data.

---

   📌 Project Overview

Tourism Experience Analytics is designed to:

- Predict user ratings for tourism destinations (Regression)
- Classify user experience sentiment (Classification)
- Recommend destinations using Collaborative Filtering (Recommendation System)

This project demonstrates a complete ML workflow including data preprocessing, model building, evaluation, and recommendation logic.

---

     🧠 Machine Learning Tasks

1️⃣ Rating Prediction (Regression)
- Model: Linear Regression
- Goal: Predict numerical rating scores for tourism experiences

2️⃣ Experience Classification
- Model: Logistic Regression / Classification Model
- Goal: Classify experience as Positive / Negative

3️⃣ Recommendation System
- Method: User-Based Collaborative Filtering
- Goal: Recommend destinations based on similar user preferences

---

 📂 Project Structure
Tourism-Experience-Analytics/
│
├── data/
│   ├── User.csv
│   ├── Type.csv
│   ├── Item.csv
│   ├── VisitMode.csv
│   ├── Transaction.csv
│   └── final_dataset.csv
│
├── generate_data.py
├── preprocessing.py
├── regression_model.py
├── classification_model.py
├── recommendation_model.py
├── main.py
│
├── requirements.txt
└── README.md

---
  📌 What Each File Should Do
🔹 generate_data.py
Creates synthetic tourism dataset

🔹 preprocessing.py

Merges datasets and creates final dataset

🔹 regression_model.py

Predicts rating (numeric)

🔹 classification_model.py 

Predicts rating category (Positive/Neutral/Negative)

🔹 recommendation_model.py

Collaborative filtering logic

🔹 main.py

Runs everything in correct order


---

   🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Jupyter Notebook

---

   🚀 Installation

Clone the repository:
git clone https://github.com/SanaXD25/Tourism-Experience-Analytics.git
https://github.com/SanaXD25/Tourism-Experience-Analytics.git

---

   📥 Install Dependencies:
pip install -r requirements.txt


---

   📊 Results

- Built regression and classification models with evaluation metrics
- Implemented a functional recommendation system
- Structured modular ML pipeline

---

   🎯 Future Improvements

- Deploy as a web application
- Add advanced recommendation algorithms
- Improve model tuning and performance

---

 👩‍💻 Author
SanaXD25
Machine Learning & Data Science Enthusiast

