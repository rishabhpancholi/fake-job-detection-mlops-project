# Imports
import yaml
from pathlib import Path
from get_project_root import root_path

# Loading params
params = yaml.safe_load(open(Path(root_path(ignore_cwd=False))/"params.yaml"))
"""Training pipeline related constants"""
ARTIFACTS_DIR: str = "artifacts"

"""Data Ingestion related constants"""
DATA_INGESTION_ZIPFILE_PATH: str = "data/fake_job_zip.zip"
DATA_INGESTION_RAW_DATA_FILE_NAME: str = "fake_job_postings.csv"
DATA_INGESTION_ID_COL: str = "job_id"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_TRAIN_FILE_NAME: str = "train.csv"
DATA_INGESTION_TEST_FILE_NAME: str = "test.csv"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = params["data_ingestion"]["TRAIN_TEST_SPLIT_RATIO"]

"""Data Transformation related constants"""
DATA_TRANSFORMATION_DIR_NAME: str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_TRAIN_FILE_NAME: str = "transformed_train.csv"
DATA_TRANSFORMATION_TRANSFORMED_TEST_FILE_NAME: str = "transformed_test.csv"

"""Model Trainer related constants"""
MODEL_TRAINER_DIR_NAME: str = "model_trainer"
MODEL_TRAINER_MODEL_FILE_NAME: str = "model.joblib"
MODEL_TRAINER_COUNT_VECTORIZER_MAX_FEATURES: int = params["model_trainer"]["COUNT_VECTORIZER_MAX_FEATURES"]
MODEL_TRAINER_MODEL_NAME: str = params["model_trainer"]["MODEL_NAME"]
MODEL_TRAINER_MODEL_PARAMS: dict = params["model_trainer"][MODEL_TRAINER_MODEL_NAME]
MODEL_TRAINER_EXPERIMENT_NAME: str = "fake_job_detection"
MODEL_TRAINER_REPO_OWNER: str = "rishabhpancholi"
MODEL_TRAINER_REPO_NAME: str = "fake-job-detection-mlops-project"
MODEL_TRAINER_TARGET_COL: str = "fraudulent"
