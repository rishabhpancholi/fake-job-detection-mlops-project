# General Imports
import pandas as pd
from sklearn.pipeline import Pipeline

# Package Imports
from api.model import ModelOutput

def give_prediction(input:pd.DataFrame, model: Pipeline)-> ModelOutput:
    """Returns the prediction for a given input"""
    fraudulent_prediction = model.predict(input)[0]
    fraudulent_probability = model.predict_proba(input)[0][1]
    non_fraudulent_probability = model.predict_proba(input)[0][0]
    return ModelOutput(
        fraudulent=fraudulent_prediction,
        fraudulent_probability=fraudulent_probability,
        non_fraudulent_probability=non_fraudulent_probability
    )