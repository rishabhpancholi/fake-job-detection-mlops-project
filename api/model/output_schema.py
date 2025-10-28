# General Imports
from typing import Annotated,Literal
from pydantic import BaseModel,Field

class ModelOutput(BaseModel):
    """Model Output Schema"""
    fraudulent: Annotated[Literal[0,1],Field(description="0/1 Prediction of whether the job is fraudulent or not")]
    fraudulent_probability: Annotated[float,Field(description="The probability of the job being fraudulent between 0 and 1")]
    non_fraudulent_probability: Annotated[float,Field(description="The probability of the job not being fraudulent between 0 and 1")]