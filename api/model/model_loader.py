# General Imports
import mlflow
from sklearn.pipeline import Pipeline

# Package Imports
from api.config import APIConfig

# APIConfig
config = APIConfig()

class ModelLoaderError(Exception):
    """Custom exception for model loading errors"""
    pass

def load_model(config: APIConfig=config)-> Pipeline:
    """Loads the model from the mlflow model registry"""
    try:
        uri = f"https://dagshub.com/{config.model_trainer_repo_owner}/{config.model_trainer_repo_name}.mlflow"
        mlflow.set_tracking_uri(uri)
        mlflow.set_registry_uri(uri)
        return mlflow.sklearn.load_model(f"models:/{config.model_name}/Production")
    except Exception as e:
        raise ModelLoaderError(f"Error occured while loading the model: {str(e)}")