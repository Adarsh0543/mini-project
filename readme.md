# US Census Income Classification Project

## 📌 Project Overview
This project is a machine learning web application that predicts whether a person's income exceeds $50K/year based on census data. Using the 1994 US Census (Adult) dataset, various classification algorithms were trained and evaluated. The final model (Random Forest) is deployed using a **Flask** web application for real-time predictions.

## 📂 Dataset
* **Source:** 1994 US Census Database.
* **Goal:** Binary classification (Income `<=50K` or `>50K`).
* **Key Features:** Age, Work Class, Education, Marital Status, Occupation, Capital Gain/Loss, Hours per Week, Native Country, Sex.

## 🛠️ Tech Stack
* **Frontend:** HTML, CSS
* **Backend:** Python, Flask
* **Machine Learning:** Scikit-learn, Pandas, NumPy
* **Serialization:** Joblib

## 📊 Model Performance Evaluation
During the training phase, several models were tested to find the best balance of accuracy and F1-score. Below are the comparative results obtained during testing:

| Model | Accuracy | Precision (Weighted) | Recall (Weighted) | F1-Score (Weighted) |
| :--- | :---: | :---: | :---: | :---: |
| **Random Forest Classifier** | **0.86** | **0.86** | **0.86** | **0.86** |
| **K-Neighbors Classifier** | 0.84 | 0.85 | 0.84 | 0.84 |
| **AdaBoost Classifier** | 0.83 | 0.83 | 0.83 | 0.83 |
| **Decision Tree Classifier** | 0.83 | 0.83 | 0.83 | 0.83 |
| **Support Vector Classifier** | 0.76 | 0.76 | 0.76 | 0.76 |
| **Naive Bayes** | 0.76 | 0.76 | 0.76 | 0.76 |
| **Logistic Regression** | 0.75 | 0.75 | 0.75 | 0.75 |

*> **Conclusion:** The **Random Forest Classifier** achieved the highest accuracy (86%) and F1-score, making it the most robust model for this dataset. It was consequently selected for the final deployment.*

