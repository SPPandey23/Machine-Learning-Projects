<h1 align="center">🌧️ Rainfall Prediction in Australia</h1>
<h3 align="center">End-to-End Machine Learning Pipeline with Streamlit Deployment</h3>

<p align="center">
Predict whether it will rain tomorrow using historical weather data.
</p>

<p align="center">
<a href="https://www.python.org/">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python Badge">
</a>
<a href="https://scikit-learn.org/">
  <img src="https://img.shields.io/badge/Scikit--Learn-Latest-orange.svg" alt="Scikit-Learn Badge">
</a>
<a href="https://streamlit.io/">
  <img src="https://img.shields.io/badge/Streamlit-App-FF4B4B.svg" alt="Streamlit Badge">
</a>
</p>

<hr>

<h2>📌 Project Description</h2>

<p>
This project builds a supervised machine learning system to predict 
<strong>RainToday (Yes/No)</strong> using Australian weather data.
</p>

<p>
A professional, end-to-end machine learning solution designed to predict rainfall in Australia. This project demonstrates a transition from experimental research (Jupyter Notebooks) to a modular, production-ready architecture with an interactive dashboard.
</p>

<p>
The core objective is to predict whether it will rain tomorrow in specific Australian regions based on a diverse set of meteorological parameters (temperature, humidity, pressure, wind speed, etc.). This repository showcases the full lifecycle of a data science project, including:
</p>

<ul>
  <li>Exploratory Data Analysis (EDA) and visualization.</li>
  <li>Robust Preprocessing Pipelines using Scikit-Learn transformers.</li>
  <li>Model Engineering featuring Random Forest and Logistic Regression.</li>
  <li>Production Deployment via a Streamlit web application.</li>
</ul>

<p>The system includes:</p>

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

<p><strong>Results Summary</strong></p>

<ul>
  <li>Primary Model: Random Forest</li>
  <li>Key Metrics: High AUC-ROC and F1-Score on the 'Rainy' class, ensuring reliable warnings for potential precipitation.</li>
</ul>

<p>Model is saved as:</p>

<pre>model.joblib</pre>

<hr>

<h2>🚀 How to Run</h2>

<h3>1️⃣ Train the Model</h3>

<pre>
python src/train.py
</pre>

<p>This will:</p>

<ul>
  <li>Load data</li>
  <li>Preprocess</li>
  <li>Train model</li>
  <li>Print evaluation metrics</li>
  <li>Save <code>model.joblib</code></li>
</ul>

<h3>2️⃣ Run the Streamlit App</h3>

<pre>
streamlit run app.py
</pre>

<p>The application will open at:</p>

<pre>http://localhost:8501</pre>

<p>Users can input:</p>

<ul>
  <li>Temperature</li>
  <li>Humidity</li>
  <li>Pressure</li>
  <li>Wind Direction & Speed</li>
  <li>Cloud cover</li>
  <li>Rain Yesterday</li>
</ul>

<p>The model outputs:</p>

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
├── FinalProject_AUSWeather.ipynb
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

<p>
This project highlights professional standards in Machine Learning operations (MLOps), focusing on code reusability, modularity, and deployment readiness—
</p>
