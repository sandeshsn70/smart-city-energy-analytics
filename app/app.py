from flask import Flask, request, jsonify, render_template
import pandas as pd
import joblib
import os

app = Flask(__name__)

# Base paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "..", "models", "energy_demand_model.pkl")
HISTORY_DIR = os.path.join(BASE_DIR, "data")
HISTORY_PATH = os.path.join(HISTORY_DIR, "prediction_history.csv")

# Create history folder if not exists
os.makedirs(HISTORY_DIR, exist_ok=True)

# Load model
model = joblib.load(MODEL_PATH)

# Save prediction history
def save_prediction(input_data, prediction):
    row = {**input_data, "predicted_energy": prediction}
    df = pd.DataFrame([row])

    if not os.path.exists(HISTORY_PATH):
        df.to_csv(HISTORY_PATH, index=False)
    else:
        df.to_csv(HISTORY_PATH, mode="a", header=False, index=False)

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    error = None
    history = None

    if request.method == "POST":
        try:
            hour = int(request.form["hour"])
            day = int(request.form["day"])
            month = int(request.form["month"])
            weekday = int(request.form["weekday"])
            is_weekend = int(request.form["is_weekend"])
            lag_1 = float(request.form["lag_1"])

            # Validation
            if not (0 <= hour <= 23):
                raise ValueError("Hour must be between 0 and 23")
            if not (1 <= day <= 31):
                raise ValueError("Day must be between 1 and 31")
            if not (1 <= month <= 12):
                raise ValueError("Month must be between 1 and 12")
            if not (0 <= weekday <= 6):
                raise ValueError("Weekday must be between 0 and 6")
            if is_weekend not in [0, 1]:
                raise ValueError("Weekend must be 0 or 1")

            data = {
                "hour": hour,
                "day": day,
                "month": month,
                "weekday": weekday,
                "is_weekend": is_weekend,
                "lag_1": lag_1
            }

            df = pd.DataFrame([data])
            prediction = round(model.predict(df)[0], 2)

            save_prediction(data, prediction)

        except Exception as e:
            error = str(e)

    # Load history
    if os.path.exists(HISTORY_PATH):
        history = pd.read_csv(HISTORY_PATH).tail(5).to_dict(orient="records")

    return render_template(
        "index.html",
        prediction=prediction,
        error=error,
        history=history
    )

@app.route("/predict", methods=["POST"])
def predict_api():
    data = request.json
    df = pd.DataFrame([data])
    prediction = model.predict(df)
    return jsonify({"predicted_energy_MW": float(prediction[0])})

if __name__ == "__main__":
    app.run(debug=True)
