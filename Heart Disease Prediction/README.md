<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Heart Disease Prediction – ML Project</title>
  <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&family=Fira+Code:wght@400;500&display=swap" rel="stylesheet"/>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: 'Nunito', sans-serif;
      background: #f9f4f4;
      color: #2c1a1a;
      font-size: 15px;
      line-height: 1.75;
    }

    /* ── HEADER ── */
    .header {
      background: #c0392b;
      padding: 48px 24px 40px;
      text-align: center;
      position: relative;
      overflow: hidden;
    }

    .header::after {
      content: '♥';
      position: absolute;
      font-size: 300px;
      right: -40px; top: -60px;
      color: rgba(255,255,255,0.06);
      pointer-events: none;
    }

    .header h1 {
      font-size: clamp(26px, 4vw, 42px);
      font-weight: 800;
      color: #fff;
      margin-bottom: 10px;
    }

    .header p {
      color: rgba(255,255,255,0.8);
      font-size: 15px;
      max-width: 500px;
      margin: 0 auto 22px;
    }

    .badge-row {
      display: flex; flex-wrap: wrap; justify-content: center; gap: 8px;
    }

    .badge {
      background: rgba(255,255,255,0.15);
      border: 1px solid rgba(255,255,255,0.25);
      color: #fff;
      font-size: 12px;
      font-weight: 700;
      padding: 4px 12px;
      border-radius: 20px;
    }

    /* ── LAYOUT ── */
    .wrap {
      max-width: 820px;
      margin: 0 auto;
      padding: 40px 20px 60px;
    }

    section { margin-bottom: 44px; }

    /* ── SECTION TITLE ── */
    .sec-title {
      display: flex; align-items: center; gap: 10px;
      margin-bottom: 16px;
    }

    .sec-icon {
      font-size: 20px;
      width: 40px; height: 40px;
      background: #fff;
      border: 2px solid #f0d0d0;
      border-radius: 10px;
      display: flex; align-items: center; justify-content: center;
      flex-shrink: 0;
    }

    .sec-title h2 {
      font-size: 20px;
      font-weight: 800;
      color: #c0392b;
    }

    p { margin-bottom: 12px; color: #3d2222; }

    hr {
      border: none;
      border-top: 2px dashed #f0d0d0;
      margin: 40px 0;
    }

    /* ── KAGGLE BOX ── */
    .kaggle-box {
      background: #fff;
      border: 2px solid #d5e8f8;
      border-radius: 12px;
      padding: 18px 20px;
      display: flex; align-items: flex-start; gap: 14px;
      margin-bottom: 16px;
    }

    .k-logo {
      background: #20beff;
      color: #fff;
      font-weight: 800;
      font-size: 16px;
      width: 44px; height: 44px;
      border-radius: 8px;
      display: flex; align-items: center; justify-content: center;
      flex-shrink: 0;
    }

    .kaggle-box h4 { font-size: 14px; font-weight: 800; color: #1a6bb5; margin-bottom: 4px; }
    .kaggle-box p  { font-size: 13.5px; color: #445; margin: 0; }

    .kaggle-box a {
      display: inline-block;
      margin-top: 8px;
      font-size: 12.5px;
      font-weight: 700;
      color: #20beff;
      text-decoration: none;
      border-bottom: 1px solid #b8e4f9;
    }
    .kaggle-box a:hover { color: #1a6bb5; }

    /* ── NOTE BOX ── */
    .note {
      background: #fff8f8;
      border-left: 4px solid #c0392b;
      border-radius: 0 8px 8px 0;
      padding: 14px 18px;
      margin: 14px 0;
      font-size: 14.5px;
      color: #3d2222;
    }

    .note strong { color: #c0392b; }

    /* ── SIMPLE CARDS ── */
    .cards {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
      gap: 14px;
    }

    .card {
      background: #fff;
      border: 2px solid #f0d8d8;
      border-radius: 12px;
      padding: 18px;
    }

    .card .icon { font-size: 26px; margin-bottom: 8px; }
    .card h4    { font-size: 14px; font-weight: 800; margin-bottom: 5px; }
    .card p     { font-size: 13px; color: #7a5555; margin: 0; }

    /* ── DATA TABLE ── */
    .tbl-wrap {
      overflow-x: auto;
      border-radius: 10px;
      border: 2px solid #f0d8d8;
    }

    table {
      width: 100%;
      border-collapse: collapse;
      background: #fff;
      font-size: 13.5px;
    }

    thead { background: #c0392b; color: #fff; }
    thead th { padding: 10px 14px; font-size: 12px; text-transform: uppercase; letter-spacing: 0.06em; text-align: left; }

    tbody td { padding: 9px 14px; border-top: 1px solid #f5e4e4; vertical-align: top; }
    tbody tr:hover td { background: #fff8f8; }

    td.col-name {
      font-family: 'Fira Code', monospace;
      font-size: 12.5px;
      color: #c0392b;
      font-weight: 500;
      white-space: nowrap;
    }

    .tag {
      display: inline-block;
      font-size: 11px;
      font-weight: 700;
      padding: 2px 8px;
      border-radius: 4px;
    }
    .tag-n { background: #e8f8f0; color: #1a7a43; }
    .tag-c { background: #eaf4ff; color: #1a6fb5; }
    .tag-b { background: #fff8e1; color: #a06000; }
    .tag-t { background: #fdecea; color: #c0392b; }

    /* ── CODE BLOCKS ── */
    pre {
      background: #1e1420;
      border-radius: 10px;
      padding: 18px 20px;
      overflow-x: auto;
      margin: 12px 0;
    }

    pre code {
      font-family: 'Fira Code', monospace;
      font-size: 13px;
      color: #cdd3db;
      line-height: 1.8;
    }

    .cm  { color: #5c6370; font-style: italic; }
    .fn  { color: #61afef; }

    code:not(pre code) {
      font-family: 'Fira Code', monospace;
      font-size: 12.5px;
      background: #fdecea;
      color: #c0392b;
      padding: 2px 6px;
      border-radius: 4px;
    }

    /* ── FILE TREE ── */
    .tree {
      background: #1e1420;
      border-radius: 10px;
      padding: 18px 22px;
      font-family: 'Fira Code', monospace;
      font-size: 13px;
      line-height: 2;
      color: #abb2bf;
    }

    .tree .dir  { color: #61afef; }
    .tree .dim  { color: rgba(171,178,191,0.4); }
    .tree .lbl  {
      font-family: 'Nunito', sans-serif;
      font-size: 10.5px;
      font-weight: 700;
      background: rgba(98,198,143,0.15);
      color: #62c68f;
      border: 1px solid rgba(98,198,143,0.3);
      padding: 1px 7px;
      border-radius: 4px;
      margin-left: 6px;
      vertical-align: middle;
    }

    /* ── STEPS ── */
    .steps { display: flex; flex-direction: column; gap: 14px; }

    .step {
      display: flex; gap: 14px; align-items: flex-start;
      background: #fff;
      border: 2px solid #f0d8d8;
      border-radius: 12px;
      padding: 16px 18px;
    }

    .step-num {
      min-width: 32px; height: 32px;
      background: #c0392b;
      color: #fff;
      border-radius: 8px;
      font-size: 14px;
      font-weight: 800;
      display: flex; align-items: center; justify-content: center;
      flex-shrink: 0;
    }

    .step h4 { font-size: 14px; font-weight: 800; margin-bottom: 4px; }
    .step p  { font-size: 13px; color: #7a5555; margin: 0; }
    .step pre { margin-top: 10px; }

    /* ── MODEL CARDS ── */
    .model-cards {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
      gap: 14px;
    }

    .model-card {
      background: #fff;
      border: 2px solid #f0d8d8;
      border-radius: 12px;
      padding: 18px;
      text-align: center;
    }

    .model-card .mi { font-size: 32px; margin-bottom: 8px; }
    .model-card h4  { font-size: 14px; font-weight: 800; margin-bottom: 6px; }
    .model-card p   { font-size: 12.5px; color: #7a5555; }

    /* ── FOOTER ── */
    footer {
      background: #2c1a1a;
      color: rgba(255,255,255,0.45);
      text-align: center;
      padding: 26px;
      font-size: 13px;
    }

    footer span { color: #e8a09a; }
  </style>
</head>
<body>

<!-- HEADER -->
<header class="header">
  <h1>❤️ Heart Disease Prediction</h1>
  <p>A beginner-friendly machine learning project that predicts heart disease from patient data.</p>
  <div class="badge-row">
    <span class="badge">🐍 Python</span>
    <span class="badge">📊 Scikit-Learn</span>
    <span class="badge">🌐 Streamlit</span>
    <span class="badge">MIT License</span>
  </div>
</header>

<div class="wrap">

  <!-- DATASET -->
  <section>
    <div class="sec-title">
      <div class="sec-icon">📦</div>
      <h2>Dataset</h2>
    </div>

    <div class="kaggle-box">
      <div class="k-logo">K</div>
      <div>
        <h4>Heart Disease Dataset — Kaggle (johnsmith88)</h4>
        <p>
          This project uses the <strong>Heart Disease Dataset</strong> by
          <strong>johnsmith88</strong> on Kaggle. It comes from the original
          Cleveland data from the UCI Machine Learning Repository.
          It contains <strong>1,025 patient records</strong> and <strong>14 columns</strong>
          of health information — no missing values, perfect for beginners!
        </p>
        <a href="https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset" target="_blank">
          🔗 View dataset on Kaggle →
        </a>
      </div>
    </div>

    <p>
      Each row represents one patient. The last column (<code>target</code>) is what we want
      to predict — <strong>1</strong> means heart disease is present, <strong>0</strong> means it is not.
    </p>
  </section>

  <hr/>

  <!-- 1. PROBLEM -->
  <section>
    <div class="sec-title">
      <div class="sec-icon">🤔</div>
      <h2>1. Problem Definition</h2>
    </div>

    <div class="note">
      <strong>The question we want to answer:</strong><br/>
      Given some basic health measurements about a patient, can a computer predict whether they have heart disease?
    </div>

    <p>
      This is called a <strong>classification problem</strong> — we're sorting patients into
      two groups: "has heart disease" or "does not have heart disease". We teach the model
      using past patient records where we already know the answer, then test it on new ones.
    </p>
  </section>

  <hr/>

  <!-- 2. DATA -->
  <section>
    <div class="sec-title">
      <div class="sec-icon">🗂️</div>
      <h2>2. Data</h2>
    </div>

    <p>
      The data originally came from the <strong>Cleveland Clinic Foundation</strong> and is one of
      the most popular datasets for learning ML. The Kaggle version we use has been cleaned up
      and is ready to use straight away — no messy preprocessing needed to get started.
    </p>

    <p>
      It has <strong>1,025 rows</strong> (patients) and <strong>14 columns</strong> (features).
      The mix of number columns and category columns gives good practice for a real ML workflow.
    </p>
  </section>

  <hr/>

  <!-- 3. EVALUATION -->
  <section>
    <div class="sec-title">
      <div class="sec-icon">🎯</div>
      <h2>3. Evaluation</h2>
    </div>

    <div class="note">
      <strong>Our goal:</strong> Reach <strong>85%+ accuracy</strong> predicting heart disease
      on unseen test data. If we hit that, we'll move forward with the project.
    </div>

    <p>We check how well our model is doing using four simple scores:</p>

    <div class="cards">
      <div class="card">
        <div class="icon">🎯</div>
        <h4>Accuracy</h4>
        <p>Out of all predictions, how many were right? e.g. 87 out of 100 = 87%</p>
      </div>
      <div class="card">
        <div class="icon">🔍</div>
        <h4>Precision</h4>
        <p>When we say "heart disease", how often are we actually correct?</p>
      </div>
      <div class="card">
        <div class="icon">📡</div>
        <h4>Recall</h4>
        <p>Of all real heart disease cases, how many did we catch? Missing one is very costly.</p>
      </div>
      <div class="card">
        <div class="icon">⚖️</div>
        <h4>F1-Score</h4>
        <p>A single number balancing both Precision and Recall together.</p>
      </div>
    </div>
  </section>

  <hr/>

  <!-- 4. FEATURES -->
  <section>
    <div class="sec-title">
      <div class="sec-icon">📋</div>
      <h2>4. Features (Data Dictionary)</h2>
    </div>

    <p>
      Here's what every column in the dataset means. Always understand your data before
      building any model — this is one of the most important habits in machine learning!
    </p>

    <div class="tbl-wrap">
      <table>
        <thead>
          <tr>
            <th>Column</th>
            <th>What it means</th>
            <th>Type</th>
            <th>Example values</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-name">age</td>
            <td>Patient's age in years</td>
            <td><span class="tag tag-n">Number</span></td>
            <td>29 – 77</td>
          </tr>
          <tr>
            <td class="col-name">sex</td>
            <td>Patient's sex</td>
            <td><span class="tag tag-c">Category</span></td>
            <td>0 = Female, 1 = Male</td>
          </tr>
          <tr>
            <td class="col-name">cp</td>
            <td>Type of chest pain felt</td>
            <td><span class="tag tag-c">Category</span></td>
            <td>0 Typical Angina · 1 Atypical · 2 Non-anginal · 3 None</td>
          </tr>
          <tr>
            <td class="col-name">trestbps</td>
            <td>Resting blood pressure on hospital admission</td>
            <td><span class="tag tag-n">Number</span></td>
            <td>mm Hg</td>
          </tr>
          <tr>
            <td class="col-name">chol</td>
            <td>Cholesterol level in the blood</td>
            <td><span class="tag tag-n">Number</span></td>
            <td>mg/dl</td>
          </tr>
          <tr>
            <td class="col-name">fbs</td>
            <td>Is fasting blood sugar above 120 mg/dl?</td>
            <td><span class="tag tag-b">Yes/No</span></td>
            <td>0 = No, 1 = Yes</td>
          </tr>
          <tr>
            <td class="col-name">restecg</td>
            <td>Resting ECG heart test result</td>
            <td><span class="tag tag-c">Category</span></td>
            <td>0 Normal · 1 ST-T issue · 2 Left ventricle issue</td>
          </tr>
          <tr>
            <td class="col-name">thalach</td>
            <td>Highest heart rate reached during exercise</td>
            <td><span class="tag tag-n">Number</span></td>
            <td>71 – 202 bpm</td>
          </tr>
          <tr>
            <td class="col-name">exang</td>
            <td>Did exercise cause chest pain (angina)?</td>
            <td><span class="tag tag-b">Yes/No</span></td>
            <td>0 = No, 1 = Yes</td>
          </tr>
          <tr>
            <td class="col-name">oldpeak</td>
            <td>ECG dip during exercise compared to rest</td>
            <td><span class="tag tag-n">Number</span></td>
            <td>0.0 – 6.2</td>
          </tr>
          <tr>
            <td class="col-name">slope</td>
            <td>Shape of the ECG line at peak exercise</td>
            <td><span class="tag tag-c">Category</span></td>
            <td>0 Up · 1 Flat · 2 Down</td>
          </tr>
          <tr>
            <td class="col-name">ca</td>
            <td>Number of major blood vessels visible</td>
            <td><span class="tag tag-n">Number</span></td>
            <td>0 – 3</td>
          </tr>
          <tr>
            <td class="col-name">thal</td>
            <td>Blood disorder type (Thalassemia)</td>
            <td><span class="tag tag-c">Category</span></td>
            <td>1 Normal · 2 Fixed Defect · 3 Reversible Defect</td>
          </tr>
          <tr>
            <td class="col-name">target ⭐</td>
            <td><strong>Does the patient have heart disease? This is what we predict.</strong></td>
            <td><span class="tag tag-t">Target</span></td>
            <td>0 = No, 1 = Yes</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>

  <hr/>

  <!-- 5. MODELLING -->
  <section>
    <div class="sec-title">
      <div class="sec-icon">🤖</div>
      <h2>5. Modelling</h2>
    </div>

    <p>
      We try three different algorithms and pick the one that performs best.
      Each has a different way of learning patterns from the data.
    </p>

    <div class="model-cards">
      <div class="model-card">
        <div class="mi">📏</div>
        <h4>Logistic Regression</h4>
        <p>Simple and fast. A great starting point. Easy to understand why it makes each prediction.</p>
      </div>
      <div class="model-card">
        <div class="mi">🌲</div>
        <h4>Random Forest</h4>
        <p>Builds many decision trees and combines their answers. Usually gives the best accuracy.</p>
      </div>
      <div class="model-card">
        <div class="mi">📍</div>
        <h4>k-Nearest Neighbors</h4>
        <p>Finds the most similar patients in training data and votes on a prediction. Very intuitive!</p>
      </div>
    </div>

    <p style="margin-top:16px;">
      We also do <strong>hyperparameter tuning</strong> — this just means trying different
      settings for each algorithm to squeeze out the best possible score.
    </p>
  </section>

  <hr/>

  <!-- 6. EXPERIMENTATION -->
  <section>
    <div class="sec-title">
      <div class="sec-icon">🧪</div>
      <h2>6. Experimentation</h2>
    </div>

    <p>
      After training, we compare all three models and see which one scores highest on data
      it has never seen before (the <strong>test set</strong>). The winner gets saved and
      used in the web app.
    </p>

    <div class="note">
      <strong>Beginner tip — Train/Test Split:</strong><br/>
      We split the data: <strong>80%</strong> is used to train the model, and
      <strong>20%</strong> is held back to test it. The model never sees the test set
      during training, so the final score is a fair measure of real-world performance.
    </div>
  </section>

  <hr/>

  <!-- PROJECT STRUCTURE -->
  <section>
    <div class="sec-title">
      <div class="sec-icon">📁</div>
      <h2>Project Structure</h2>
    </div>

    <p>Here's how everything is organised. Each file has one clear job:</p>

    <div class="tree">
      <div><span class="dir">heart-disease-predictor/</span></div>
      <div><span class="dim">├── </span><span class="dir">src/</span><span class="dim">  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# All the Python code</span></div>
      <div><span class="dim">│   ├── </span>data_ingestion.py<span class="dim">    # Loads the CSV file</span></div>
      <div><span class="dim">│   ├── </span>data_preprocessing.py<span class="dim"> # Cleans &amp; prepares data</span></div>
      <div><span class="dim">│   ├── </span>eda.py<span class="dim">               # Makes charts to explore data</span></div>
      <div><span class="dim">│   ├── </span>hyperparameter.py<span class="dim">    # Finds best settings for models</span></div>
      <div><span class="dim">│   ├── </span>model_training.py<span class="dim">    # Trains the models</span></div>
      <div><span class="dim">│   ├── </span>model_evaluation.py<span class="dim">  # Checks how accurate they are</span></div>
      <div><span class="dim">│   ├── </span>model_saving.py<span class="dim">      # Saves the best model to disk</span></div>
      <div><span class="dim">│   ├── </span>feature_importance.py<span class="dim"> # Shows which features matter most</span></div>
      <div><span class="dim">│   └── </span>pipeline.py<span class="dim">          # Runs all steps in order</span><span class="lbl">START HERE</span></div>
      <div><span class="dim">├── </span>heart.csv<span class="dim">            # The dataset from Kaggle</span></div>
      <div><span class="dim">├── </span>main.py<span class="dim">              # The Streamlit web app</span><span class="lbl">WEB APP</span></div>
      <div><span class="dim">├── </span>requirements.txt<span class="dim">     # Libraries you need to install</span></div>
      <div><span class="dim">└── </span>README.md</div>
    </div>
  </section>

  <hr/>

  <!-- HOW TO RUN -->
  <section>
    <div class="sec-title">
      <div class="sec-icon">🚀</div>
      <h2>How to Run This Project</h2>
    </div>

    <div class="steps">
      <div class="step">
        <div class="step-num">1</div>
        <div>
          <h4>Download the code</h4>
          <p>Clone or download this repository to your computer.</p>
          <pre><code><span class="fn">git</span> clone &lt;your-repo-url&gt;
<span class="fn">cd</span> heart-disease-predictor</code></pre>
        </div>
      </div>

      <div class="step">
        <div class="step-num">2</div>
        <div>
          <h4>Create a virtual environment</h4>
          <p>This keeps your project's libraries separate from other Python projects on your computer.</p>
          <pre><code><span class="fn">python</span> -m venv venv
<span class="fn">source</span> venv/bin/activate    <span class="cm"># Mac / Linux</span>
venv\Scripts\activate        <span class="cm"># Windows</span></code></pre>
        </div>
      </div>

      <div class="step">
        <div class="step-num">3</div>
        <div>
          <h4>Install the required libraries</h4>
          <p>This reads the <code>requirements.txt</code> file and installs everything at once.</p>
          <pre><code><span class="fn">pip</span> install -r requirements.txt</code></pre>
        </div>
      </div>

      <div class="step">
        <div class="step-num">4</div>
        <div>
          <h4>Train the model</h4>
          <p>Runs the full pipeline — loads data, trains all 3 models, finds the best one, and saves it.</p>
          <pre><code><span class="fn">python</span> -m src.pipeline</code></pre>
        </div>
      </div>

      <div class="step">
        <div class="step-num">5</div>
        <div>
          <h4>Open the web app</h4>
          <p>Launches a browser page where you type in patient details and get a prediction instantly!</p>
          <pre><code><span class="fn">streamlit</span> run main.py</code></pre>
        </div>
      </div>
    </div>
  </section>

  <hr/>

  <!-- LICENSE -->
  <section>
    <div class="sec-title">
      <div class="sec-icon">📄</div>
      <h2>License</h2>
    </div>
    <p>
      This project is open source under the <strong>MIT License</strong> —
      feel free to use, modify, and share it. See the <code>LICENSE</code> file for details.
    </p>
    <p style="font-size:13.5px; color:#7a5555;">
      Dataset from the UCI Machine Learning Repository, Cleveland Clinic Foundation.
      Available on Kaggle:
      <a href="https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset"
         style="color:#c0392b;" target="_blank">
        kaggle.com/datasets/johnsmith88/heart-disease-dataset
      </a>
    </p>
  </section>

</div>

<footer>
  <p>Made with <span>♥</span> for learning machine learning · Heart Disease Prediction Project</p>
</footer>

</body>
</html>