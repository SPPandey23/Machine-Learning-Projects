<h1 align="center">❤️ Heart Disease Prediction</h1>

<p align="center">
A beginner-friendly machine learning project that predicts heart disease from patient data.
</p>

<p align="center">
🐍 Python • 📊 Scikit-Learn • 🌐 Streamlit • MIT License
</p>

<hr>

<h2>📦 Dataset</h2>

<p>
This project uses the <strong>Heart Disease Dataset</strong> by <strong>johnsmith88</strong> on Kaggle.
It originates from the Cleveland dataset of the UCI Machine Learning Repository.
The dataset contains <strong>1,025 patient records</strong> and <strong>14 columns</strong> of structured health information.
There are no missing values.
</p>

<p>
🔗 
<a href="https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset" target="_blank">
View Dataset on Kaggle
</a>
</p>

<p>
Each row represents one patient. The <code>target</code> column is the prediction variable:
</p>

<ul>
  <li><code>1</code> → Heart disease present</li>
  <li><code>0</code> → No heart disease</li>
</ul>

<hr>

<h2>🎯 Problem Definition</h2>

<p>
Given structured clinical measurements, can we predict whether a patient has heart disease?
</p>

<p>
This is a <strong>binary classification problem</strong>. The model is trained on historical patient data
with known outcomes and evaluated on unseen test data.
</p>

<hr>

<h2>📊 Evaluation Metrics</h2>

<ul>
  <li><strong>Accuracy:</strong> Overall correctness of predictions</li>
  <li><strong>Precision:</strong> Correct positive predictions out of all predicted positives</li>
  <li><strong>Recall:</strong> Correctly detected positive cases out of all actual positives</li>
  <li><strong>F1-Score:</strong> Harmonic mean of Precision and Recall</li>
</ul>

<hr>

<h2>📋 Feature Overview</h2>

<table>
<tr>
<th>Feature</th>
<th>Description</th>
<th>Type</th>
</tr>

<tr><td>age</td><td>Age of patient</td><td>Numeric</td></tr>
<tr><td>sex</td><td>Gender (0 = Female, 1 = Male)</td><td>Category</td></tr>
<tr><td>cp</td><td>Chest pain type</td><td>Category</td></tr>
<tr><td>trestbps</td><td>Resting blood pressure</td><td>Numeric</td></tr>
<tr><td>chol</td><td>Cholesterol level</td><td>Numeric</td></tr>
<tr><td>fbs</td><td>Fasting blood sugar &gt; 120 mg/dl</td><td>Binary</td></tr>
<tr><td>restecg</td><td>Resting ECG results</td><td>Category</td></tr>
<tr><td>thalach</td><td>Maximum heart rate achieved</td><td>Numeric</td></tr>
<tr><td>exang</td><td>Exercise-induced angina</td><td>Binary</td></tr>
<tr><td>oldpeak</td><td>ST depression induced by exercise</td><td>Numeric</td></tr>
<tr><td>slope</td><td>Slope of peak exercise ST segment</td><td>Category</td></tr>
<tr><td>ca</td><td>Number of major vessels</td><td>Numeric</td></tr>
<tr><td>thal</td><td>Thalassemia type</td><td>Category</td></tr>
<tr><td><strong>target</strong></td><td><strong>Heart disease presence (0/1)</strong></td><td>Target</td></tr>

</table>

<hr>

<h2>🤖 Models Implemented</h2>

<ul>
  <li><strong>Logistic Regression</strong></li>
  <li><strong>Random Forest</strong></li>
  <li><strong>k-Nearest Neighbors</strong></li>
</ul>

<p>
Hyperparameter tuning was performed to optimize performance.
</p>

<hr>

<h2>🧪 Experimentation</h2>

<ul>
  <li>80% Training Data</li>
  <li>20% Testing Data</li>
</ul>

<p>
The test set is strictly separated from training to ensure unbiased evaluation.
</p>

<hr>

<h2>📁 Project Structure</h2>

<pre>
heart-disease-predictor/
│
├── src/
│   ├── data_ingestion.py
│   ├── data_preprocessing.py
│   ├── eda.py
│   ├── hyperparameter.py
│   ├── model_training.py
│   ├── model_evaluation.py
│   ├── model_saving.py
│   ├── feature_importance.py
│   └── pipeline.py
│
├── heart.csv
├── main.py
├── requirements.txt
└── README.md
</pre>

<hr>

<h2>🚀 How to Run</h2>

<pre><code>git clone &lt;your-repo-url&gt;
cd heart-disease-predictor
</code></pre>

<pre><code>python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
</code></pre>

<pre><code>pip install -r requirements.txt
</code></pre>

<pre><code>python -m src.pipeline
</code></pre>

<pre><code>streamlit run main.py
</code></pre>

<hr>

<h2>📄 License</h2>

<p>
This project is licensed under the <strong>MIT License</strong>.
</p>

<p>
Dataset Source:
<a href="https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset" target="_blank">
kaggle.com/datasets/johnsmith88/heart-disease-dataset
</a>
</p>
