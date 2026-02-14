# Rainfall Prediction Project

This project predicts whether it will rain tomorrow in Australia based on weather data. It uses a Random Forest Classifier trained on data from Melbourne, Melbourne Airport, and Watsonia.

## Project Structure

- `data/`: Contains the dataset (downloaded automatically).
- `src/`: Source code for data loading, processing, model definition, and training.
- `app.py`: Streamlit web application.
- `requirements.txt`: Python dependencies.

## Setup and Installation

1.  Clone the repository or download the files.
2.  Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Training the Model

To train the model (and download the data if needed), run:

```bash
python -m src.train
```

This will create a `model.joblib` file in the root directory.

## Running the Web App

To start the Streamlit application:

```bash
streamlit run app.py
```

## Model Details

- **Algorithm**: Random Forest Classifier
- **Features**: MinTemp, MaxTemp, Rainfall, Evaporation, Sunshine, WindGustSpeed, WindSpeed9am, WindSpeed3pm, Humidity9am, Humidity3pm, Pressure9am, Pressure3pm, Cloud9am, Cloud3pm, Temp9am, Temp3pm, Location, WindGustDir, WindDir9am, WindDir3pm, RainYesterday, season.
- **Preprocessing**: StandardScaler for numerical features, OneHotEncoder for categorical features.
