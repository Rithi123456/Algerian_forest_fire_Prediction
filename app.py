import pickle
import numpy as np
import pandas as pd

from flask import Flask, render_template, request

application = Flask(__name__)
app = application

# ==================================
# GLOBAL VARIABLE
# ==================================

latest_prediction = {}

# ==================================
# LOAD MODEL & SCALER
# ==================================

loaded_model = pickle.load(
    open('Algerian_forest_fires_model.pkl', 'rb')
)

loaded_scaler = pickle.load(
    open('Algerian_forest_fires_scaler.pkl', 'rb')
)

# ==================================
# HOME PAGE
# ==================================

@app.route("/")
def index():
    return render_template('index.html')


# ==================================
# PREDICTION PAGE
# ==================================

@app.route('/prediction')
def prediction():
    return render_template('prediction.html')


# ==================================
# ANALYTICS PAGE
# ==================================

@app.route('/analytics')
def analytics():

    global latest_prediction

    df = pd.read_csv(
        'Algerian_forest_fires_cleaned_dataset.csv'
    )

    df['Classes'] = (
        df['Classes']
        .astype(str)
        .str.strip()
        .str.lower()
    )

    total_records = len(df)

    avg_temp = round(
        df['Temperature'].mean(),
        2
    )

    avg_fwi = round(
        df['FWI'].mean(),
        2
    )

    fire_cases = (
        df['Classes'] == 'fire'
    ).sum()

    region_counts = (
        df['Region']
        .value_counts()
        .sort_index()
        .tolist()
    )

    return render_template(
        'analytics.html',
        total_records=total_records,
        avg_temp=avg_temp,
        avg_fwi=avg_fwi,
        fire_cases=fire_cases,
        region_counts=region_counts,
        latest_prediction=latest_prediction,
        temperature=latest_prediction.get("temperature", 0),
        humidity=latest_prediction.get("humidity", 0),
        windspeed=latest_prediction.get("windspeed", 0),
        rain=latest_prediction.get("rain", 0),
        prediction_score=latest_prediction.get("prediction", 0)
    )


# ==================================
# PREDICTION LOGIC
# ==================================

@app.route('/predictdata', methods=['POST'])
def predict_datapoint():

    global latest_prediction

    try:

        Temperature = float(
            request.form.get('Temperature')
        )

        RH = float(
            request.form.get('RH')
        )

        Ws = float(
            request.form.get('Ws')
        )

        Rain = float(
            request.form.get('Rain')
        )

        FFMC = float(
            request.form.get('FFMC')
        )

        DMC = float(
            request.form.get('DMC')
        )

        ISI = float(
            request.form.get('ISI')
        )

        Classes = float(
            request.form.get('Classes')
        )

        Region = float(
            request.form.get('Region')
        )

        data = np.array([[
            Temperature,
            RH,
            Ws,
            Rain,
            FFMC,
            DMC,
            ISI,
            Classes,
            Region
        ]])

        scaled_data = loaded_scaler.transform(
            data
        )

        prediction = loaded_model.predict(
            scaled_data
        )[0]

        if prediction < 10:

            risk = "🟢 LOW"

            recommendation = (
                "Low fire risk. Continue routine monitoring."
            )

        elif prediction < 20:

            risk = "🟡 MODERATE"

            recommendation = (
                "Moderate fire risk. Exercise caution."
            )

        elif prediction < 30:

            risk = "🟠 HIGH"

            recommendation = (
                "High fire risk. Increase surveillance."
            )

        else:

            risk = "🔴 EXTREME"

            recommendation = (
                "Extreme fire risk. Emergency response recommended."
            )

        latest_prediction = {
            "prediction": round(prediction, 2),
            "risk": risk,
            "temperature": Temperature,
            "humidity": RH,
            "windspeed": Ws,
            "rain": Rain,
            "region": Region
        }

        return render_template(
            'prediction.html',
            prediction=round(prediction, 2),
            risk=risk,
            recommendation=recommendation
        )

    except Exception as e:

        return render_template(
            'prediction.html',
            prediction=f"Error: {str(e)}",
            risk="",
            recommendation=""
        )


# ==================================
# RUN APPLICATION
# ==================================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )