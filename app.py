import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load model and encoders
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("encoders.pkl", "rb") as f:
    encoders = pickle.load(f)

st.title(" House Price Prediction App")
st.markdown("Enter the details below to estimate your house price:")

# Input fields
area = st.number_input("Area (in sq ft)", min_value=500, max_value=20000, value=7420)
bedrooms = st.number_input("Number of Bedrooms", min_value=1, max_value=10, value=4)
bathrooms = st.number_input("Number of Bathrooms", min_value=1, max_value=10, value=2)
stories = st.number_input("Number of Stories", min_value=1, max_value=10, value=3)

mainroad = st.selectbox("Main Road Access", ["yes", "no"])
guestroom = st.selectbox("Guest Room Available", ["yes", "no"])
basement = st.selectbox("Basement", ["yes", "no"])
hotwaterheating = st.selectbox("Hot Water Heating", ["yes", "no"])
airconditioning = st.selectbox("Air Conditioning", ["yes", "no"])
parking = st.number_input("Parking Spaces", min_value=0, max_value=5, value=2)
prefarea = st.selectbox("Preferred Area", ["yes", "no"])
furnishingstatus = st.selectbox("Furnishing Status", ["furnished", "semi-furnished", "unfurnished"])

# Prepare input for prediction
input_data = pd.DataFrame({
    'area': [area],
    'bedrooms': [bedrooms],
    'bathrooms': [bathrooms],
    'stories': [stories],
    'mainroad': [mainroad],
    'guestroom': [guestroom],
    'basement': [basement],
    'hotwaterheating': [hotwaterheating],
    'airconditioning': [airconditioning],
    'parking': [parking],
    'prefarea': [prefarea],
    'furnishingstatus': [furnishingstatus]
})

# Encode categorical columns using saved encoders
for col, encoder in encoders.items():
    input_data[col] = encoder.transform(input_data[col])

# Predict button
if st.button("Predict Price"):
    prediction = model.predict(input_data)[0]
    st.success(f" Estimated House Price: ₹ {prediction:,.2f}")
