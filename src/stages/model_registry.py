# General Imports
import sys
import mlflow
import dagshub
import warnings

# Package Imports
from src.constants import *
from src.utils import Utility
from src.logging import get_logger
from src.exception import CustomException

# Ignore warnings
warnings.filterwarnings("ignore")

class ModelRegistry:
    """Class for model registry stage"""
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise CustomException(e,sys)
