import streamlit as st
from joblib import load
from numpy import array

# Load the trained model
model = load("model.pkl")

# Customizing the page layout
st.set_page_config(page_title="Placement Package Predictor", page_icon="📊")

# Styling
st.markdown("""
<style>
.main {
    background-color: #F4F4F4;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
}
.stTextInput, .stNumberInput, .stButton > button {
    font-size: 16px !important;
}
.stNumberInput input {
    padding: 10px;
    border-radius: 5px;
}
.stButton > button {
    background-color: #4CAF50 !important;
    color: white !important;
    border-radius: 5px;
    padding: 10px 20px;
}
</style>
""", unsafe_allow_html=True)

# App title
st.title("Placement Package Calculator")

# Input section
st.write("Enter CGPA")
cgpa_input = st.number_input("CGPA",
                             max_value=10.0,
                             min_value=0.0,
                             step=0.1)

# Prediction logic
if st.button("Predict"): 
    inputf = array([[cgpa_input]])
    prediction = model.predict(inputf)[0]
    prediction_value = float(prediction)  # Convert to Python float
    st.success(f"Predicted Package: {prediction_value:.2f}")