# General Imports
import streamlit as st

def home():
    """Returns the home page of the app"""
    try:
        st.write("# Welcome to Real/Fake Job Detection App! 👋")
        st.write(
                """
                This is a simple app to detect real or fake job postings using **NLP** and **ML** models.
                """
        )
        st.write(
                """
                How to use the app:
                - Enter the details of the job posting in the form on the **Prediction** tab.
                - Click on the **Predict** button.
                - The app will display the prediction for the job posting as either **Real** or **Fake**. 
                - It will also display the probability of the job being real or fake.
                """
        )
    except Exception as e:
        st.error(f"⚠️ An unexpected error occurred. Please try again later: {str(e)}")