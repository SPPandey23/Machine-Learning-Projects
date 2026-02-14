import streamlit as st
import pandas as pd
import joblib
import os
from src.utils import date_to_season
from datetime import date

# Set page config
st.set_page_config(page_title="Rainfall Prediction App", layout="wide")

@st.cache_resource
def load_model():
    if os.path.exists('model.joblib'):
        return joblib.load('model.joblib')
    else:
        st.error("Model file 'model.joblib' not found. Please run src/train.py first.")
        return None

def main():
    st.title("🌧️ Rainfall Prediction in Australia")
    st.markdown("Predict whether it will rain tomorrow based on today's weather data.")

    model = load_model()
    if model is None:
        return

    # Sidebar Inputs
    st.sidebar.header("Input Parameters")
    
    location = st.sidebar.selectbox("Location", ['Melbourne', 'MelbourneAirport', 'Watsonia'])
    input_date = st.sidebar.date_input("Date", date.today())
    season = date_to_season(pd.to_datetime(input_date))
    st.sidebar.write(f"Season: **{season}**")
    
    rain_yesterday = st.sidebar.selectbox("Did it Rain Yesterday?", ['No', 'Yes'])
    
    st.sidebar.subheader("Wind")
    wind_gust_dir = st.sidebar.selectbox("Wind Gust Direction", ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW'])
    wind_dir_9am = st.sidebar.selectbox("Wind Direction 9am", ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW'])
    wind_dir_3pm = st.sidebar.selectbox("Wind Direction 3pm", ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW'])
    
    wind_gust_speed = st.sidebar.number_input("Wind Gust Speed (km/h)", value=40.0)
    wind_speed_9am = st.sidebar.number_input("Wind Speed 9am (km/h)", value=15.0)
    wind_speed_3pm = st.sidebar.number_input("Wind Speed 3pm (km/h)", value=20.0)

    st.sidebar.subheader("Temperature & Rainfall")
    min_temp = st.sidebar.number_input("Min Temp (°C)", value=10.0)
    max_temp = st.sidebar.number_input("Max Temp (°C)", value=20.0)
    rainfall = st.sidebar.number_input("Rainfall (mm)", value=0.0)
    evaporation = st.sidebar.number_input("Evaporation (mm)", value=5.0)
    sunshine = st.sidebar.number_input("Sunshine (hours)", value=8.0)
    
    st.sidebar.subheader("Humidity & Pressure")
    humidity_9am = st.sidebar.number_input("Humidity 9am (%)", value=60.0)
    humidity_3pm = st.sidebar.number_input("Humidity 3pm (%)", value=50.0)
    pressure_9am = st.sidebar.number_input("Pressure 9am (hPa)", value=1015.0)
    pressure_3pm = st.sidebar.number_input("Pressure 3pm (hPa)", value=1012.0)
    
    st.sidebar.subheader("Cloud & Temp")
    cloud_9am = st.sidebar.number_input("Cloud 9am (oktas)", value=4.0)
    cloud_3pm = st.sidebar.number_input("Cloud 3pm (oktas)", value=4.0)
    temp_9am = st.sidebar.number_input("Temp 9am (°C)", value=15.0)
    temp_3pm = st.sidebar.number_input("Temp 3pm (°C)", value=18.0)

    # Prepare input for prediction
    input_data = pd.DataFrame({
        'MinTemp': [min_temp],
        'MaxTemp': [max_temp],
        'Rainfall': [rainfall],
        'Evaporation': [evaporation],
        'Sunshine': [sunshine],
        'WindGustSpeed': [wind_gust_speed],
        'WindSpeed9am': [wind_speed_9am],
        'WindSpeed3pm': [wind_speed_3pm],
        'Humidity9am': [humidity_9am],
        'Humidity3pm': [humidity_3pm],
        'Pressure9am': [pressure_9am],
        'Pressure3pm': [pressure_3pm],
        'Cloud9am': [cloud_9am],
        'Cloud3pm': [cloud_3pm],
        'Temp9am': [temp_9am],
        'Temp3pm': [temp_3pm],
        'Location': [location],
        'WindGustDir': [wind_gust_dir],
        'WindDir9am': [wind_dir_9am],
        'WindDir3pm': [wind_dir_3pm],
        'RainYesterday': [rain_yesterday],
        'season': [season]
    })

    if st.button("Predict Rainfall"):
        try:
            prediction = model.predict(input_data)[0]
            probability = model.predict_proba(input_data)[0]
            
            st.subheader("Prediction")
            if prediction == 'Yes':
                st.error(f"🌧️ Yes, it is likely to rain. ({probability[1]*100:.1f}%)")
            else:
                st.success(f"☀️ No, it is unlikely to rain. ({probability[0]*100:.1f}%)")
                
        except Exception as e:
            st.error(f"Error making prediction: {e}")

if __name__ == "__main__":
    main()
