# ⚡ Smart City Energy Analytics & Demand Prediction

An end-to-end **Data Analysis + Data Science + Web Application** project that analyzes
hourly energy consumption data and predicts future energy demand using machine learning.
The project also includes a **Flask-based web dashboard** with validation, charts, and
prediction history.

---

## 📌 Project Overview

Smart cities generate large volumes of energy consumption data, but without proper
analysis, it is difficult to identify patterns and plan energy usage efficiently.

This project:
- Performs **exploratory data analysis (EDA)** on time-series energy data
- Builds **machine learning models** to predict energy demand
- Deploys predictions using a **Flask REST API**
- Provides a **modern web UI** for user interaction, visualization, and history tracking

---

## 🎯 Objectives

- Analyze hourly energy consumption trends
- Identify peak and off-peak usage patterns
- Perform feature engineering on time-based data
- Train and evaluate machine learning models
- Deploy the model using Flask with an interactive UI
- Visualize prediction history using charts

---

## 🧠 Why This Project Is Strong for Resume

✔ Combines **Data Analysis + Data Science + Deployment**  
✔ Real-world **Smart City** use case  
✔ Covers **EDA, ML, API, UI, and visualization**  
✔ Industry-standard project structure  
✔ Excellent discussion scope for interviews  

---

## 🛠️ Tech Stack

- **Programming Language**: Python  
- **Data Analysis**: Pandas, NumPy  
- **Visualization**: Matplotlib, Seaborn, Chart.js  
- **Machine Learning**: Scikit-learn (Linear Regression, Random Forest)  
- **Web Framework**: Flask  
- **Notebook**: Jupyter Notebook  
- **Version Control**: Git & GitHub  

---

## 📂 Project Structure

```text
smart-city-energy-analytics/
│
├── data/
│   ├── raw/                    # Raw datasets (AEP_hourly.csv)
│   └── processed/              # Cleaned & feature-engineered data
│
├── notebooks/
│   ├── 01_data_cleaning_and_eda.ipynb
│   ├── 02_feature_engineering.ipynb
│   └── 03_model_building.ipynb
│
├── models/
│   └── energy_demand_model.pkl  # Generated locally (not tracked on GitHub)
│
├── app/
│   ├── app.py                  # Flask application
│   ├── templates/
│   │   └── index.html          # Modern UI (HTML/CSS/JS)
│   └── data/
│       └── prediction_history.csv
│
├── requirements.txt
└── README.md
