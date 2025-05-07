# 🛌 Sleep Quality Classification

This project is a machine learning classification model that predicts **Sleep Quality** (Poor, Okay, Good, Excellent) based on various lifestyle and health-related inputs. The model is trained on a Kaggle dataset and deployed using **Streamlit** for real-time user interaction.

---

## 📊 Dataset Overview

- **Source**: [Kaggle](https://www.kaggle.com/)
- **Size**: 5,000 entries × 15 columns
- **Target Variable**: `Sleep Quality` (1–10), categorized into 4 classes:
  - 1–3 → Poor
  - 4–5 → Okay
  - 6–7 → Good
  - 8–10 → Excellent

### 📁 Features:

- Date
- Person_ID
- Age
- Gender
- Sleep Start Time
- Sleep End Time
- Total Sleep Hours
- **Sleep Quality** (Target)
- Exercise (mins/day)
- Caffeine Intake (mg)
- Screen Time Before Bed (mins)
- Work Hours (hrs/day)
- Productivity Score
- Mood Score
- Stress Level

---

## 🧠 Why Categorize Sleep Quality?

Although the original target was a 1–10 score, it was **converted into 4 categorical classes** to simplify the task into a classification problem. This approach is:

- More interpretable for real users
- Suitable for classification models
- Helps balance model complexity and accuracy

---

## ⚙️ Model Training

### Algorithms Tried:

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier
- XGBoost
- **LightGBM** ✅ (Best)

### ✅ Best Model: **LightGBM**

- **Accuracy**: `0.892`

### 📈 Evaluation:

- During training: `classification_report` (precision, recall, f1-score)
- On Streamlit app: Only accuracy score is shown for simplicity

---

## 🛠 Feature Engineering

Several preprocessing steps were performed:

- Encoding categorical variables (`Gender`)
- Categorizing `Sleep Quality`
- Normalizing / scaling numerical features (if needed)
- Dropping irrelevant or duplicate fields (`Date`, `Person_ID`)

---

## 🚀 Deployment

The best-performing model (LightGBM) is:

- Saved as a `.joblib` file
- Integrated into a **Streamlit** web application
- Takes user input and displays predicted Sleep Quality with accuracy

---

## ⚠️ Known limitations:

Predictions tend to skew towards "Poor" or "Okay" — model needs further tuning or balancing.

Accuracy score is calculated in training, but not yet displayed in the deployed app (small Streamlit issue I'm fixing soon).

## Contact

Feel free to reach out if you have any questions or suggestions:
gmail: s.y.shavkatbekov@gmail.com
