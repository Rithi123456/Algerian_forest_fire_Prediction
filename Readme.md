# Algerian Forest Fire Prediction System

## Project Overview

The **Algerian Forest Fire Prediction System** is an end-to-end Machine Learning web application designed to predict the **Fire Weather Index (FWI)** using meteorological and environmental parameters.

This project combines **Machine Learning, Data Analytics, Flask Web Development, Docker, Jenkins, and AWS Deployment** to build a complete forest fire risk intelligence system.

The application allows users to:

- Predict forest fire risk based on environmental inputs
- Analyze fire risk using a trained machine learning model
- Visualize prediction factors using interactive analytics charts
- Explore historical dataset insights through dashboard analytics
- Deploy the application using Docker and Jenkins CI/CD

---

## Features

### Forest Fire Prediction

Users can input environmental factors such as:

- Temperature
- Relative Humidity (RH)
- Wind Speed (Ws)
- Rain
- Fine Fuel Moisture Code (FFMC)
- Duff Moisture Code (DMC)
- Initial Spread Index (ISI)
- Fire Class
- Region

The system predicts:

- **Fire Weather Index (FWI)**

Risk Level Classification:

- Low Risk
- Moderate Risk
- High Risk
- Extreme Risk

---

### Analytics Dashboard

The analytics dashboard provides:

- Latest prediction analysis
- Prediction factor visualization using Chart.js
- Historical dataset insights
- Fire vs Non-Fire distribution
- Region-wise fire occurrence analysis

---

## Dataset Description

The project uses the **Algerian Forest Fires Dataset**, containing weather and fire-related measurements from two Algerian regions:

- Bejaia
- Sidi-Bel Abbes

### Features

- Temperature
- Relative Humidity (RH)
- Wind Speed (Ws)
- Rain
- FFMC
- DMC
- ISI
- Classes
- Region

### Target Variable

- Fire Weather Index (FWI)

---

## Machine Learning Workflow

### Data Preprocessing

- Dataset cleaning
- Null value handling
- Feature selection
- Label encoding
- Train-test split
- Feature scaling using StandardScaler

### Exploratory Data Analysis

- Statistical analysis
- Correlation heatmap
- Feature relationship analysis
- Fire occurrence distribution

### Models Implemented

- Linear Regression
- Ridge Regression (RidgeCV)
- Lasso Regression (LassoCV)
- Elastic Net Regression (ElasticNetCV)

---

## Model Performance

| Model             | MAE    | R² Score |
| ----------------- | ------ | -------- |
| Linear Regression | 0.5468 | 0.9848   |
| RidgeCV           | 0.5642 | 0.9843   |
| ElasticNetCV      | 0.5782 | 0.9839   |
| LassoCV           | 0.7085 | 0.9783   |

### Best Performing Model

**Linear Regression**

- MAE: 0.5468
- R² Score: 0.9848

The model achieved the best overall performance with high prediction accuracy and low error rate.

---

## Tech Stack

### Backend

- Python
- Flask
- NumPy
- Pandas
- Scikit-Learn

### Frontend

- HTML
- CSS
- JavaScript
- Chart.js

### Deployment

- Docker
- Jenkins
- AWS EC2

### Model Serialization

- Pickle

---

## Project Structure

```bash
Algerian_forest_fire_Prediction/
│── app.py
│── requirements.txt
│── README.md
│── Dockerfile
│── Jenkinsfile
│── Algerian_forest_fires_model.pkl
│── Algerian_forest_fires_scaler.pkl
│── Algerian_forest_fires_cleaned_dataset.csv
│── Algerian_forest_fires_dataset_UPDATE.csv
│
├── templates/
│   ├── index.html
│   ├── prediction.html
│   ├── analytics.html
│   └── about.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
└── Notebooks/
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Rithi123456/Algerian_forest_fire_Prediction.git
```

Move into project directory:

```bash
cd Algerian_forest_fire_Prediction
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Flask application:

```bash
python app.py
```

---

## Docker Deployment

Build Docker image:

```bash
docker build -t forestfire .
```

Run Docker container:

```bash
docker run -d -p 5000:5000 --name forestfire forestfire
```

Access application:

```bash
http://localhost:5000
```

---

## Jenkins CI/CD Pipeline

This project includes a Jenkins pipeline for:

- Cloning the GitHub repository
- Building the Docker image
- Running the Flask application inside a Docker container
- Automated deployment on AWS EC2

Pipeline stages:

- Clone Repository
- Build Docker Image
- Deploy Container

---

## Author

**Rithick M**
