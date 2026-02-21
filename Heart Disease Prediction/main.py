import streamlit as st
import joblib
import pandas as pd

st.set_page_config(page_title="Heart Disease Predictor")

st.title("Heart Disease Prediction App")

package = joblib.load("best_model.joblib")

model = package["model"]
feature_info = package["feature_info"]

st.write("Enter patient information:")

user_input = {}

for feature, info in feature_info.items():

    unique_vals = info["unique_values"]

    if len(unique_vals) <= 5:
        user_input[feature] = st.selectbox(
            feature,
            sorted(unique_vals)
        )
    else:
        user_input[feature] = st.number_input(
            feature,
            value=0.0
        )

if st.button("Predict"):

    input_df = pd.DataFrame([user_input])

    prediction = model.predict(input_df)[0]

    probability = None
    if hasattr(model, "predict_proba"):
        probability = model.predict_proba(input_df)[0][1]

    st.subheader("Result")

    if prediction == 1:
        st.error("Heart Disease Detected")
    else:
        st.success("No Heart Disease Detected")

    if probability is not None:
        st.write(f"Probability: {probability:.2f}")