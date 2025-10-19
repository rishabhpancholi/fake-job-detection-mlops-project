# General Imports
import sys
import numpy as np
import pandas as pd
from zlib import crc32
from pathlib import Path
from zipfile import ZipFile

# Package Imports
from src.constants import *
from src.utils import Utility
from src.logging import get_logger
from src.exception import CustomException

class DataIngestion:
    """Class for data ingestion stage"""
    def __init__(self, logger = get_logger('data_ingestion'),utils = Utility()):
        """Initializes the data ingestion class"""
        try:
            self.zipfile_path = Path(DATA_INGESTION_ZIPFILE_PATH)
            self.raw_data_file_name = DATA_INGESTION_RAW_DATA_FILE_NAME
            self.train_test_split_ratio = DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
            self.id_col = DATA_INGESTION_ID_COL
            self.train_df_file_path = Path(ARTIFACTS_DIR)/DATA_INGESTION_DIR_NAME/DATA_INGESTION_TRAIN_FILE_NAME
            self.test_df_file_path = Path(ARTIFACTS_DIR)/DATA_INGESTION_DIR_NAME/DATA_INGESTION_TEST_FILE_NAME
            self.utils = utils
            self.log = logger
            self.log.info("Data Ingestion started")
        except Exception as e:
            raise CustomException(e,sys)
        
    def load_data(self)-> pd.DataFrame:
        """Loads the data"""
        try:
            self.log.info("Loading the data")
            with ZipFile(self.zipfile_path) as zip:
                with zip.open(self.raw_data_file_name) as f:
                    df = pd.read_csv(f)
            self.log.info("Data loaded successfully")
            return df
        except Exception as e:
            raise CustomException(e,sys)
        
    def split_data(self, df:pd.DataFrame)-> tuple[pd.DataFrame,pd.DataFrame]:
        """Splits the data into train and test dataframes"""
        try:
            self.log.info("Splitting the data")
            ids = df[self.id_col]
            in_test_set = ids.apply(lambda id_: crc32(np.int64(id_)) & 0xffffffff < self.train_test_split_ratio * 2**32)
            self.log.info("Data splitted successfully")
            return df.loc[~in_test_set].drop(columns=[self.id_col]),df.loc[in_test_set].drop(columns=[self.id_col])
        except Exception as e:
            raise CustomException(e,sys)

    def ingest(self):
        """Ingests the data"""
        try:
            df = self.load_data()
            train_df,test_df = self.split_data(df)
            self.log.info("Saving the dataframes to csv files")
            self.utils.save_data(train_df,self.train_df_file_path)
            self.utils.save_data(test_df,self.test_df_file_path)
            self.log.info("Dataframes saved successfully")
        except Exception as e:
            raise CustomException(e,sys)

if __name__ == "__main__":
    data_ingestion = DataIngestion()
    data_ingestion.ingest()

