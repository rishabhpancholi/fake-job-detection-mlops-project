# General Imports
import sys

# Package imports
from src.utils import save_data
from src.logging import get_logger
from src.exception import CustomException
from src.components import ZipFileIngestor
from src.entities import DataIngestionArtifact

logger = get_logger(name='data_ingestion') # Creates a logger

class DataIngestion:
    """Class for data ingestion"""
    def __init__(self):
        try:
            logger.info("Initiating data ingestion")
            self.data_ingestor = ZipFileIngestor()
        except Exception as e:
            raise CustomException(e,sys)

    def ingest(self):
        """Method for ingesting data"""
        try:
            logger.info("Ingesting data")
            self.data_ingestor.connect()
            df = self.data_ingestor.load_data()
            df = self.data_ingestor.clean_data(df=df)
            train_df,test_df = self.data_ingestor.split_data(df=df)
            save_data(train_df,self.data_ingestor.data_ingestion_config.train_file_path)
            save_data(test_df,self.data_ingestor.data_ingestion_config.test_file_path)
            self.data_ingestor.close()
            logger.info("Data ingestion completed")

            data_ingestion_artifact  = DataIngestionArtifact(
                train_file_path=self.data_ingestor.data_ingestion_config.train_file_path,
                test_file_path=self.data_ingestor.data_ingestion_config.test_file_path
            )
            return data_ingestion_artifact
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__ == "__main__":
    data_ingestion = DataIngestion()
    data_ingestion.ingest()