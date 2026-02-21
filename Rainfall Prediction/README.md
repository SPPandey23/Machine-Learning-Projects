
<h1 align="center">🌧️ Rainfall Prediction in Australia</h1>
<h3 align="center">End-to-End Machine Learning Pipeline with Streamlit Deployment</h3>

<p align="center">
Predict whether it will rain tomorrow using historical weather data.
</p>

<hr>

<h2>📌 Project Description</h2>

<p>
This project builds a supervised machine learning system to predict 
<strong>RainToday (Yes/No)</strong> using Australian weather data.
</p>

<p>
The system includes:
</p>

<ul>
  <li>Data loading from cloud-hosted CSV</li>
  <li>Preprocessing & feature engineering</li>
  <li>Scikit-Learn pipeline construction</li>
  <li>Model training & evaluation</li>
  <li>Model serialization using Joblib</li>
  <li>Interactive Streamlit web application</li>
</ul>

<hr>

<h2>🏗️ Project Architecture</h2>

<pre>
Data (CSV URL)
        ↓
Preprocessing (Cleaning + Feature Engineering)
        ↓
ColumnTransformer (Scaling + OneHot Encoding)
        ↓
RandomForestClassifier
        ↓
Model Evaluation
        ↓
model.joblib
        ↓
Streamlit Web App
</pre>

<hr>

<h2>🧠 Machine Learning Details</h2>

<h3>Data Preprocessing</h3>

<ul>
  <li>Removes missing values using <code>dropna()</code></li>
  <li>Filters selected locations:
    <ul>
      <li>Melbourne</li>
      <li>MelbourneAirport</li>
      <li>Watsonia</li>
    </ul>
  </li>
  <li>Renames:
    <ul>
      <li>RainToday → RainYesterday</li>
      <li>RainTomorrow → RainToday (Target)</li>
    </ul>
  </li>
  <li>Feature Engineering:
    <ul>
      <li>Extract season from Date column</li>
    </ul>
  </li>
</ul>

<hr>

<h3>Model Pipeline</h3>

<p>
The project uses a <strong>Scikit-Learn Pipeline</strong> with a 
<code>ColumnTransformer</code>.
</p>

<h4>Numerical Features</h4>
<ul>
  <li>StandardScaler</li>
</ul>

<h4>Categorical Features</h4>
<ul>
  <li>OneHotEncoder (handle_unknown='ignore')</li>
</ul>

<h4>Classifier</h4>

<pre>
RandomForestClassifier(
    n_estimators=100,
    max_depth=20,
    min_samples_split=2,
    random_state=42
)
</pre>

<hr>

<h2>📊 Model Evaluation</h2>

<ul>
  <li>Train-Test Split (80/20)</li>
  <li>Accuracy Score</li>
  <li>Classification Report (Precision, Recall, F1)</li>
</ul>

Model is saved as:

<pre>model.joblib</pre>

<hr>

<h2>🚀 How to Run</h2>

<h3>1️⃣ Train the Model</h3>

<pre>
python src/train.py
</pre>

This will:
<ul>
  <li>Load data</li>
  <li>Preprocess</li>
  <li>Train model</li>
  <li>Print evaluation metrics</li>
  <li>Save <code>model.joblib</code></li>
</ul>

<hr>

<h3>2️⃣ Run the Streamlit App</h3>

<pre>
streamlit run app.py
</pre>

The application will open at:

<pre>http://localhost:8501</pre>

Users can input:
<ul>
  <li>Temperature</li>
  <li>Humidity</li>
  <li>Pressure</li>
  <li>Wind Direction & Speed</li>
  <li>Cloud cover</li>
  <li>Rain Yesterday</li>
</ul>

The model outputs:
<ul>
  <li>Prediction (Yes/No)</li>
  <li>Probability (%)</li>
</ul>

<hr>

<h2>📂 Project Structure</h2>

<pre>
rainfall-prediction/
│
├── src/
│   ├── data_loader.py
│   ├── model.py
│   ├── train.py
│   ├── utils.py
│   └── __init__.py
│
├── app.py
├── model.joblib
├── requirements.txt
└── README.md
</pre>

<hr>

<h2>🛠 Tech Stack</h2>

<ul>
  <li>Python</li>
  <li>Pandas</li>
  <li>Scikit-Learn</li>
  <li>Streamlit</li>
  <li>Joblib</li>
</ul>

<hr>

<h2>📈 Key Features</h2>

<ul>
  <li>End-to-end ML pipeline</li>
  <li>Feature engineering (Season extraction)</li>
  <li>Production-style modular structure</li>
  <li>Interactive prediction interface</li>
  <li>Reusable training script</li>
</ul>

<hr>

<p align="center">
⭐ If you found this project useful, consider giving it a star.
</p>
=======
# 🌧️ Rainfall Prediction in Australia: Productionized ML Pipeline

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Latest-orange.svg)](https://scikit-learn.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B.svg)](https://streamlit.io/)

A professional, end-to-end machine learning solution designed to predict rainfall in Australia. This project demonstrates a transition from experimental research (Jupyter Notebooks) to a modular, production-ready architecture with an interactive dashboard.

---

## 🚀 Project Overview

The core objective is to predict whether it will rain tomorrow in specific Australian regions based on a diverse set of meteorological parameters (temperature, humidity, pressure, wind speed, etc.). This repository showcases the full lifecycle of a data science project, including:

*   **Exploratory Data Analysis (EDA)** and visualization.
*   **Robust Preprocessing Pipelines** using Scikit-Learn transformers.
*   **Model Engineering** featuring Random Forest and Logistic Regression.
*   **Production Deployment** via a Streamlit web application.

## 🛠️ Key Technical Features

*   **Modular Architecture**: Clean separation of concerns between data ingestion, model training, and inference.
*   **Scikit-Learn Pipelines**: Integrated handling of missing values, scaling, and categorical encoding ensuring no data leakage.
*   **Feature Engineering**: Custom transformers for seasonal trend analysis and regional specificities.
*   **Interactive Dashboard**: Real-time prediction interface with probability scoring.

## 📁 Repository Structure

```tree
.
├── app.py                  # Main Streamlit application
├── src/                    # Core modular logic
│   ├── data_loader.py      # Reliable data ingestion and cleaning
│   ├── model.py            # Model definition and pipeline architecture
│   ├── train.py            # Automated training script
│   └── utils.py            # Technical helper functions
├── FinalProject_AUSWeather.ipynb # EDA and model experimentation
├── model.joblib            # Serialized production model artifact
├── requirements.txt        # Reproducible environment configuration
└── README.md               # Documentation
```

## 🧪 Machine Learning Workflow

### 1. Preprocessing & Engineering
- **Encoding**: One-Hot Encoding for categorical meteorological data (Wind Direction, Location).
- **Scaling**: Standardisation of continuous variables for model stability.
- **Handling Imbalance**: Analysis performed on class distributions to ensure model fairness.

### 2. Modeling
The system utilizes a **Random Forest Classifier** as its primary engine, chosen for its robustness against outliers and ability to capture complex non-linear relationships in weather patterns.

## 🚦 Getting Started

### Prerequisites
- Python 3.8+
- pip

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/[your-username]/Rainfall-Prediction.git
   cd Rainfall-Prediction
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Project
- **Launch the App**:
  ```bash
  streamlit run app.py
  ```
- **Retrain the Model**:
  ```bash
  python src/train.py
  ```

## 📊 Results Summary
- **Primary Model**: Random Forest
- **Key Metrics**: High AUC-ROC and F1-Score on the 'Rainy' class, ensuring reliable warnings for potential precipitation.

---

## 👨‍💻 Developer Focus
This project highlights professional standards in Machine Learning operations (MLOps), focusing on code reusability, modularity, and deployment readiness—
