import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('models/model.pkl')  # Adjust the path to your model

# Streamlit UI
st.title("Insurance Prediction App")
st.write("Provide the necessary details to predict insurance outcomes.")

# User input form
with st.form("prediction_form"):
    Gender = st.selectbox("Gender", options=["Male", "Female"])
    Age = st.number_input("Age", min_value=18, max_value=100, step=1)
    HasDrivingLicense = st.selectbox("Has Driving License", options=[0, 1])
    RegionID = st.number_input("Region ID", min_value=0.0, step=0.1)
    Switch = st.selectbox("Switch", options=[-1, 0, 1])
    PastAccident = st.selectbox("Past Accident", options=["Unknown", "No", "Yes"])
    AnnualPremium = st.number_input("Annual Premium", min_value=0.0, step=0.01)
    
    submit = st.form_submit_button("Predict")

# Process prediction
if submit:
    # Create a DataFrame from user inputs
    input_data = pd.DataFrame({
        "Gender": [Gender],
        "Age": [Age],
        "HasDrivingLicense": [HasDrivingLicense],
        "RegionID": [RegionID],
        "Switch": [Switch],
        "PastAccident": [PastAccident],
        "AnnualPremium": [AnnualPremium]
    })
    
    # Predict using the model
    try:
        prediction = model.predict(input_data)
        st.success(f"The predicted class is: {int(prediction[0])}")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
