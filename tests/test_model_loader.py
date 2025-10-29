# General Imports
import pytest
from sklearn.pipeline import Pipeline

# Package Imports
from api import load_model

def test_load_model():
    """Test the load_model function"""
    model = load_model()
    assert isinstance(model, Pipeline)