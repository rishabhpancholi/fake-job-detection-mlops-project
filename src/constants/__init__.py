import yaml

params = yaml.safe_load(open("params.yaml")) # Load the params

"""General constants"""
ARTIFACTS_DIR_NAME: str = "artifacts"
TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"

"""Data ingestion related constants"""
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_RAW_DATA_ZIP_FILE_PATH: str = "data/fake_job_zip.zip"
DATA_INGESTION_RAW_DATA_FILE_NAME:str = "fake_job_postings.csv"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = params["data_ingestion"]["TRAIN_TEST_RATIO"]

"""Data validation related constants"""
DATA_VALIDATION_DIR_NAME: str = "data_validation"