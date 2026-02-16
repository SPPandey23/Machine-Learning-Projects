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
