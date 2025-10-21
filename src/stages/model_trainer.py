# General Imports
import sys
import mlflow
import dagshub
import warnings
import pandas as pd
from pathlib import Path
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from sklearn.metrics import f1_score
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer

# Package Imports
from src.constants import *
from src.utils import Utility
from src.logging import get_logger
from src.exception import CustomException

# Ignore warnings
warnings.filterwarnings("ignore")

class ModelTrainer:
    """Class for model trainer stage"""
    def __init__(self, logger = get_logger('model_trainer'), utils = Utility()):
        """Initializes the model trainer class"""
        try:
            self.transformed_train_file_path = Path(ARTIFACTS_DIR)/DATA_TRANSFORMATION_DIR_NAME/DATA_TRANSFORMATION_TRANSFORMED_TRAIN_FILE_NAME
            self.transformed_test_file_path = Path(ARTIFACTS_DIR)/DATA_TRANSFORMATION_DIR_NAME/DATA_TRANSFORMATION_TRANSFORMED_TEST_FILE_NAME
            self.model_file_path = Path(ARTIFACTS_DIR)/MODEL_TRAINER_DIR_NAME/MODEL_TRAINER_MODEL_FILE_NAME
            self.target_col = MODEL_TRAINER_TARGET_COL
            self.count_vectorizer_max_features = MODEL_TRAINER_COUNT_VECTORIZER_MAX_FEATURES
            self.model_name = MODEL_TRAINER_MODEL_NAME
            self.registered_model_name = MODEL_TRAINER_REGISTERED_MODEL_NAME
            self.model_params = MODEL_TRAINER_MODEL_PARAMS
            self.mlflow_experiment_name = MODEL_TRAINER_EXPERIMENT_NAME
            self.dagshub_repo_owner = MODEL_TRAINER_REPO_OWNER
            self.dagshub_repo_name = MODEL_TRAINER_REPO_NAME
            self.utils = utils
            self.log = logger
            dagshub.init(repo_owner=self.dagshub_repo_owner,repo_name=self.dagshub_repo_name,mlflow =True)
            mlflow.set_experiment(self.mlflow_experiment_name)
            self.log.info("Model Trainer started")
        except Exception as e:
            raise CustomException(e,sys)
        
    def build_model_pipeline(self)-> Pipeline:
        """Builds the model pipeline"""
        try:
            self.log.info("Building the model pipeline")
            column_transformer = ColumnTransformer(
                transformers = [
                    ("encoder",OneHotEncoder(sparse_output = False,drop='first'),['salary_range', 'employment_type', 'required_experience', 'required_education']),
                    ("vectorizer",CountVectorizer(max_features = self.count_vectorizer_max_features),'text')
                ]
            )
            model_dict = {
               "xgboost": XGBClassifier,
               "lightgbm": LGBMClassifier,
               "random_forest": RandomForestClassifier
            }
            model = model_dict[self.model_name](**self.model_params)
            model_pipeline = Pipeline(
                steps = [
                    ("column_transformer",column_transformer),
                    ("model",model)
                ]
            )
            self.log.info("Pipeline built successfully")
            return model_pipeline
        except Exception as e:
            raise CustomException(e,sys)
        
    def train_model(self, X_train: pd.DataFrame, y_train: pd.Series, model_pipeline: Pipeline):
        """Trains the model"""
        try:
            self.log.info("Training the model")
            model_pipeline.fit(X_train,y_train)
            self.log.info("Model trained successfully")
        except Exception as e:
            raise CustomException(e,sys)
        
    def log_experiment(self, model_pipeline: Pipeline, X_train: pd.DataFrame, y_train: pd.Series, X_test: pd.DataFrame, y_test: pd.Series):
        """Logs the parameters and the metrics of the model"""
        try:
            self.log.info("Logging the parameters,metrics and model")
            mlflow.log_params(self.model_params)
            y_train_pred = model_pipeline.predict(X_train)
            y_test_pred = model_pipeline.predict(X_test)
            train_f1_score = f1_score(y_train, y_train_pred, pos_label=1)
            test_f1_score = f1_score(y_test, y_test_pred, pos_label=1)
            mlflow.log_metrics({"train_f1_score":train_f1_score,"test_f1_score":test_f1_score})
            signature = mlflow.models.signature.infer_signature(X_train,y_train_pred)
            mlflow.sklearn.log_model(sk_model=model_pipeline,artifact_path="model",signature=signature,registered_model_name=self.registered_model_name)
            self.log.info("Parameters,metrics and model logged successfully")
        except Exception as e:
            raise CustomException(e,sys)
        
    def train(self):
        """Trains the model"""
        try:
            train_df = self.utils.load_data(self.transformed_train_file_path)
            test_df = self.utils.load_data(self.transformed_test_file_path)
            X_train = train_df.drop(columns = [self.target_col],axis = 1)
            y_train = train_df[self.target_col]
            X_test = test_df.drop(columns = [self.target_col],axis = 1)
            y_test = test_df[self.target_col]
            model_pipeline = self.build_model_pipeline()
            self.train_model(X_train,y_train,model_pipeline)
            self.log_experiment(model_pipeline,X_train,y_train,X_test,y_test)
            self.utils.save_joblib_file(model_pipeline,self.model_file_path)
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__ == "__main__":
    model_trainer = ModelTrainer()
    model_trainer.train()