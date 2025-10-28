# General Imports
import spacy
from fastapi import APIRouter
from sklearn.pipeline import Pipeline

# Package Imports
from api.config import APIConfig
from api.model import load_model,ModelInput,ModelOutput
from api.services import give_prediction,preprocess_input_data

# Load Spacy Model
nlp = spacy.load("en_core_web_sm",disable=['parser','ner','textcat'])

# Load Model
model = load_model(config=APIConfig())

prediction_router = APIRouter()

# Prediction Route
@prediction_router.post("/predict",tags=["Prediction"])
def predict(input:ModelInput,model=model,nlp=nlp)-> ModelOutput:
    """Returns the prediction for a given input"""
    input_dict = input.model_dump()
    preprocessed_input = preprocess_input_data(input_dict=input_dict,nlp=nlp)
    prediction = give_prediction(input=preprocessed_input,model=model)
    return prediction