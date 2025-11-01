# Imports
from pydantic_settings import BaseSettings,SettingsConfigDict

class APIConfig(BaseSettings):
    """API Config class"""
    model_trainer_repo_name: str
    model_trainer_repo_owner: str
    model_name: str
    mlflow_tracking_username: str
    mlflow_tracking_password: str
    aws_access_key_id: str
    aws_secret_access_key: str
    
    model_config = SettingsConfigDict(env_file=".env")
    
