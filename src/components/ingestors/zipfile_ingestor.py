# General Imports
import sys
import pandas as pd
from zipfile import ZipFile

# Package imports
from src.base import BaseIngestor
from src.exception import CustomException

class ZipFileIngestor(BaseIngestor):
    """Class for ingesting data from a zip file"""

    def connect(self):
        """Connects to the zip file"""
        try:
            self.zip_file = ZipFile(self.data_ingestion_config.raw_data_zip_file_path)
        except Exception as e:
            raise CustomException(e,sys) 

    def load_data(self)->pd.DataFrame:
        """Loads data from the zip file"""
        try:
            return pd.read_csv(self.zip_file.open(self.data_ingestion_config.raw_data_file_name))
        except Exception as e:
            raise CustomException(e,sys)
    
    def close(self):
        """Closes the zip file"""
        try:
            self.zip_file.close()
        except Exception as e:
            raise CustomException(e,sys)

    



