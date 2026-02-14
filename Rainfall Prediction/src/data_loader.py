import pandas as pd
from src.utils import date_to_season

def load_data(url="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/_0eYOqji3unP1tDNKWZMjg/weatherAUS-2.csv"):
    df = pd.read_csv(url)
    return df

def preprocess_data(df):

    
    df = df.dropna()

    selected_locations = ['Melbourne', 'MelbourneAirport', 'Watsonia']
    df = df[df['Location'].isin(selected_locations)]


    
    df = df.rename(columns={'RainToday': 'RainYesterday', 'RainTomorrow': 'RainToday'})

    # Feature Engineering: Season
    df['Date'] = pd.to_datetime(df['Date'])
    df['season'] = df['Date'].apply(date_to_season)

    return df

def get_X_y(df):

    features = [
        'MinTemp', 'MaxTemp', 'Rainfall', 'Evaporation', 'Sunshine', 
        'WindGustSpeed', 'WindSpeed9am', 'WindSpeed3pm', 'Humidity9am', 'Humidity3pm', 
        'Pressure9am', 'Pressure3pm', 'Cloud9am', 'Cloud3pm', 'Temp9am', 'Temp3pm',
        'Location', 'WindGustDir', 'WindDir9am', 'WindDir3pm', 'RainYesterday', 'season'
    ]
    target = 'RainToday'

    X = df[features]
    y = df[target]

    return X, y
