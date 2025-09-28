# General Imports
from pathlib import Path

# Package imports
from src.constants import *

class TrainingPipelineConfig:
    def __init__(self):
        self.train_file_path:str = TRAIN_FILE_NAME
        self.test_file_path:str = TEST_FILE_NAME
        self.artifacts_folder:str = ARTIFACTS_DIR_NAME

class DataIngestionConfig:
    def __init__(self, training_pipeline_config:TrainingPipelineConfig):
        self.data_ingestion_dir_name:str = DATA_INGESTION_DIR_NAME
        self.raw_data_zip_file_path:Path = Path(DATA_INGESTION_RAW_DATA_ZIP_FILE_PATH)
        self.raw_data_file_name:str = DATA_INGESTION_RAW_DATA_FILE_NAME
        self.train_test_split_ratio:float = DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
        self.train_file_path:Path = Path(training_pipeline_config.artifacts_folder)/self.data_ingestion_dir_name/training_pipeline_config.train_file_path
        self.test_file_path:Path = Path(training_pipeline_config.artifacts_folder)/self.data_ingestion_dir_name/training_pipeline_config.test_file_path
        