# General Imports
import sys
import mlflow
import warnings
from mlflow.tracking import MlflowClient

# Package Imports
from src.constants import *
from src.utils import Utility
from src.logging import get_logger
from src.exception import CustomException

# Ignore warnings
warnings.filterwarnings("ignore")

class ModelPromotion:
    """Class for model promotion stage"""
    def __init__(self, logger = get_logger('model_promotion'), utils = Utility()):
        try:
            self.registered_model_name = MODEL_TRAINER_REGISTERED_MODEL_NAME
            self.dagshub_repo_owner = MODEL_TRAINER_REPO_OWNER
            self.dagshub_repo_name = MODEL_TRAINER_REPO_NAME
            self.utils = utils
            self.log = logger
            self.uri = f"https://dagshub.com/{self.dagshub_repo_owner}/{self.dagshub_repo_name}.mlflow"
            mlflow.set_tracking_uri(self.uri)
            mlflow.set_registry_uri(self.uri)
            self.client = MlflowClient()
            self.log.info("Model Promotion started")
        except Exception as e:
            raise CustomException(e,sys)
        
    def fetch_metrics_and_compare(self):
        """Fetches the metrics and compares them"""
        try:
            self.log.info("Fetching the model metrics and comparing them with the Production model metrics")
            versions = self.client.search_model_versions(f"name='{self.registered_model_name}'")
            latest_version = max(versions, key=lambda v: int(v.version))
            production_version = [v for v in versions if v.current_stage == "Production"][0]
            latest_version_run = self.client.get_run(latest_version.run_id)
            production_version_run = self.client.get_run(production_version.run_id)
            latest_version_metrics = latest_version_run.data.metrics.get("test_f1_score")
            production_version_metrics = production_version_run.data.metrics.get("test_f1_score")
            if latest_version_metrics >= production_version_metrics:
                self.log.info("Latest model metrics are better than the production model metrics")
                return True
            else:
                self.log.info("Latest model metrics are not better than the production model metrics")
                return False
        except Exception as e:
            raise CustomException(e,sys)

    def promote_model(self):
        """Promotes the model"""
        try:
            self.log.info("Promoting the model")
            versions = self.client.search_model_versions(f"name='{self.registered_model_name}'")
            latest_version = max(versions, key=lambda v: int(v.version)).version
            production_version = [v for v in versions if v.current_stage == "Production"][0].version
            self.client.transition_model_version_stage(name=self.registered_model_name,version=latest_version,stage="Production")
            self.client.transition_model_version_stage(name=self.registered_model_name,version=production_version,stage="Archived")
            self.log.info("Model promoted successfully")
        except Exception as e:
            raise CustomException(e,sys)
        
    def promotion_flow(self):
        """Promotes the model if the latest model metrics are better than the production model metrics"""
        try:
            if self.fetch_metrics_and_compare():
                self.promote_model()
        except Exception as e:
            raise CustomException(e,sys)

        
if __name__ == "__main__":
    model_promotion = ModelPromotion()
    model_promotion.promotion_flow()

            
