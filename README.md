# Smart City Energy Analytics & Demand Prediction

## 📌 Project Overview
This project analyzes smart city energy consumption data to identify usage patterns
and predict future energy demand using data analysis and machine learning techniques.

## 🎯 Objectives
- Analyze historical energy consumption data
- Identify peak and non-peak usage patterns
- Build predictive models for energy demand forecasting
- Visualize insights for decision-making

## 🛠️ Tech Stack
- Python (Pandas, NumPy)
- Matplotlib, Seaborn
- Scikit-learn
- Jupyter Notebook
- Flask (for deployment)
- GitHub

## 📂 Project Structure
## 📂 Project Structure

```text
smart-city-energy-analytics/
│
├── data/
│   ├── raw/                # Raw datasets
│   └── processed/          # Cleaned datasets
│
├── notebooks/
│   ├── 01_data_cleaning_and_eda.ipynb
│   ├── 02_feature_engineering.ipynb
│   └── 03_model_building.ipynb
│
├── models/
│   └── energy_demand_model.pkl
│
├── app/
│   └── app.py              # Flask application
│
├── dashboards/
│   └── screenshots/        # EDA & dashboard images
│
├── requirements.txt
└── README.md

---

## 📊 Data Analysis (EDA)
- Handled missing values and inconsistent data
- Analyzed hourly, daily, and monthly energy usage
- Identified peak demand periods
- Visualized consumption trends using graphs and charts

---

## 🤖 Data Science & Machine Learning
- Performed feature engineering on time-based data
- Built and evaluated machine learning models
- Compared model performance using evaluation metrics
- Predicted future energy demand

**Models Used:**
- Linear Regression  
- Random Forest Regressor  
- (Future) Time Series Models – ARIMA / Prophet  

---

## 📈 Visualizations
- Energy usage trends
- Peak vs non-peak demand analysis
- Correlation analysis
- Model prediction vs actual values

(Visualization screenshots are available in the `dashboards/` folder)

---

## 🚀 How to Run the Project Locally
```bash
git clone https://github.com/sandeshsn70/smart-city-energy-analytics.git
cd smart-city-energy-analytics
pip install -r requirements.txt
