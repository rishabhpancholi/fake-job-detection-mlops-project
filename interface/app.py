# General Imports
import streamlit as st

# Package Imports
from services.home_page import home
from services.prediction_page import prediction

if __name__ == "__main__":
    try:
        st.set_page_config(
            layout="wide"
        )
        tab1,tab2 = st.tabs(["Home","Prediction"])

        with tab1:
            home()
            
        with tab2:
            prediction()
    except Exception as e:
        st.error(f"⚠️ An unexpected error occurred. Please try again later: {str(e)}")
        