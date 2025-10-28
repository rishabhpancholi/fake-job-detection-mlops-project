# General Imports
import requests
import streamlit as st

# Package Imports
from utils.input_format import InputFormat

class APICallError(Exception):
    """Exception class for API call related errors"""
    pass

@st.cache_data(show_spinner="Fetching your predictions")
def get_predictions(input: InputFormat)-> dict:
    """Returns the predictions for a given input"""
    try:
        response = requests.post("https://fake-job-detection-mlops-project.onrender.com/predict",json=input.model_dump(exclude=[
            "title",
            "location",
            "department",
            "company_profile",
            "description",
            "requirements",
            "benefits",
            "industry",
            "function"
        ]))
        return response.json()
    except requests.exceptions.RequestException as e:
        raise APICallError(f"Failed to get predictions: {str(e)}")
    except Exception as e:
        raise APICallError(f"Some unexpected error occured: {str(e)}")