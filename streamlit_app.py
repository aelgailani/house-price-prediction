# streamlit_app.py
import streamlit as st
import pandas as pd
import joblib  # For loading the trained model
from xgboost import XGBRegressor

# Load the trained model
# Ensure you have the model saved as 'xgb_model.pkl' in the same directory
model = joblib.load('xgb_model.pkl')

# Define the Streamlit app
st.title("House Price Prediction App")
st.write("""
### Enter the details below to predict the house price
""")

# Collect user inputs for each feature
overall_qual = st.slider("Overall Quality (1-10)", min_value=1, max_value=10, value=5)
gr_liv_area = st.number_input("Above Ground Living Area (square feet)", value=1500)
garage_cars = st.slider("Garage Cars", min_value=0, max_value=4, value=2)
year_built = st.number_input("Year Built", min_value=1800, max_value=2024, value=2000)
total_bsmt_sf = st.number_input("Total Basement Area (square feet)", value=800)
first_flr_sf = st.number_input("First Floor Area (square feet)", value=1200)
full_bath = st.slider("Number of Full Bathrooms", min_value=0, max_value=3, value=2)
garage_area = st.number_input("Garage Area (square feet)", value=400)
lot_area = st.number_input("Lot Area (square feet)", value=7000)

# Create a DataFrame with the user inputs
input_data = pd.DataFrame({
    'OverallQual': [overall_qual],
    'GrLivArea': [gr_liv_area],
    'GarageCars': [garage_cars],
    'YearBuilt': [year_built],
    'TotalBsmtSF': [total_bsmt_sf],
    '1stFlrSF': [first_flr_sf],
    'FullBath': [full_bath],
    'GarageArea': [garage_area],
    'LotArea': [lot_area]
})

# Make predictions
prediction = model.predict(input_data)

# Display the prediction
st.subheader("Predicted Sale Price:")
st.write(f"${prediction[0]:,.2f}")