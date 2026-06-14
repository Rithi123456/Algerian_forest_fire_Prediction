# Algerian Forest Fire Prediction System

## Project Overview

The **Algerian Forest Fire Prediction System** is an end-to-end machine learning web application designed to predict the **Fire Weather Index (FWI)** using meteorological and environmental parameters.

This project combines **Machine Learning, Data Analytics, and Flask Web Development** to provide a complete forest fire risk intelligence system.

The application allows users to:

* Predict forest fire risk based on real-time environmental inputs
* Analyze fire risk using a trained machine learning model
* Visualize prediction factors using interactive analytics charts
* Explore historical dataset insights through dashboard analytics


## Features

### Forest Fire Prediction

Users can input environmental factors such as:

* Temperature
* Relative Humidity (RH)
* Wind Speed (Ws)
* Rain
* Fine Fuel Moisture Code (FFMC)
* Duff Moisture Code (DMC)
* Initial Spread Index (ISI)
* Fire Class
* Region

The system predicts:

* **Fire Weather Index (FWI)**
* Risk Level Classification:

  * Low Risk
  * Moderate Risk
  * High Risk
  * Extreme Risk

### Analytics Dashboard

The analytics dashboard provides:

* Latest prediction analysis
* Input factor visualization using Chart.js
* Historical dataset insights
* Fire vs Non-Fire distribution
* Region-wise fire occurrence analysis

## Dataset Description

The project uses the **Algerian Forest Fires Dataset**, containing weather and fire-related measurements from two Algerian regions:

* Bejaia
* Sidi-Bel Abbes

### Features:

* Temperature
* Relative Humidity (RH)
* Wind Speed (Ws)
* Rain
* FFMC
* DMC
* ISI
* Classes
* Region

### Target Variable:

* Fire Weather Index (FWI)

## Machine Learning Workflow

### Data Preprocessing

* Dataset cleaning
* Null value handling
* Feature selection
* Label encoding
* Train-test split
* Feature scaling using StandardScaler


### Exploratory Data Analysis

* Statistical analysis
* Correlation heatmap
* Feature relationship analysis
* Fire occurrence distribution


### Models Implemented

* Linear Regression
* Ridge Regression (RidgeCV)
* Lasso Regression (LassoCV)
* Elastic Net Regression (ElasticNetCV)


## Model Performance

| Model             | MAE    | R² Score |
| ----------------- | ------ | -------- |
| Linear Regression | 0.5468 | 0.9848   |
| RidgeCV           | 0.5642 | 0.9843   |
| ElasticNetCV      | 0.5782 | 0.9839   |
| LassoCV           | 0.7085 | 0.9783   |

### Best Model

**Linear Regression**

* MAE: 0.5468
* R² Score: 0.9848


## Tech Stack

### Backend

* Python
* Flask
* NumPy
* Pandas
* Scikit-Learn

### Frontend

* HTML
* CSS
* JavaScript
* Chart.js

### Model Serialization

* Pickle


## Project Structure

Algerian_forest_fire_Prediction/
│── app.py
│── requirements.txt
│── README.md
│── Algerian_forest_fires_model.pkl
│── Algerian_forest_fires_scaler.pkl
│── Algerian_forest_fires_cleaned_dataset.csv
│
├── Templates/
│   ├── index.html
│   ├── prediction.html
│   ├── analytics.html
│   └── about.html
│
├── Static/
│   ├── css/
│   ├── js/
│   └── images/
│
└── Notebooks/




## Installation

Clone the repository:

bash
git clone https://github.com/Rithi123456/Algerian_forest_fire_Prediction.git


Move into project directory:

bash
cd Algerian_forest_fire_Prediction


Install dependencies:

bash
pip install -r requirements.txt


Run the Flask app:

bash
python app.py


## Author

Rithick M
