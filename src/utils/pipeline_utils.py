# General Imports
import sys
import joblib
import pandas as pd
from pathlib import Path
from sklearn.pipeline import Pipeline

# Package Imports        
from src.exception import CustomException

class Utility:
    """Utility class for the training pipeline"""

    @staticmethod
    def save_data(df: pd.DataFrame, file_path: Path):
        """Saves the dataframe to a csv file"""
        try:
            file_path.parent.mkdir(exist_ok=True, parents=True)
            df.to_csv(file_path, index=False)
        except Exception as e:
            raise CustomException(e,sys)
        
    @staticmethod
    def load_data(path: Path)-> pd.DataFrame:
        """Loads the dataframe from a csv file"""
        try:
            return pd.read_csv(path)
        except Exception as e:
            raise CustomException(e,sys)
        
    @staticmethod
    def save_joblib_file(model: Pipeline, path: Path):
        """Saves the model to a joblib file"""
        try:
            path.parent.mkdir(exist_ok=True, parents=True)
            return joblib.dump(model,path)
        except Exception as e:
            raise CustomException(e,sys)
        
    @staticmethod
    def load_joblib_file(path: Path):
        """Loads the model from a joblib file"""
        try:
            return joblib.load(path)
        except Exception as e:
            raise CustomException(e,sys)
        