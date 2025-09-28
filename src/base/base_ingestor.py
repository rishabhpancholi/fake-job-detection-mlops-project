# General Imports
import sys
import numpy as np
import pandas as pd
from zlib import crc32
from typing import Tuple
from abc import ABC,abstractmethod

# Package imports
from src.exception import CustomException
from src.entity import TrainingPipelineConfig,DataIngestionConfig

class BaseIngestor(ABC):
    """Base class for data ingestors"""

    def __init__(self):
        try:
            self.training_pipeline_config:TrainingPipelineConfig = TrainingPipelineConfig()
            self.data_ingestion_config:DataIngestionConfig = DataIngestionConfig(training_pipeline_config=self.training_pipeline_config)
        except Exception as e:
            raise CustomException(e,sys)

    @abstractmethod
    def connect(self):        
        pass

    @abstractmethod
    def load_data(self)->pd.DataFrame:
        pass

    def split_data(self,df: pd.DataFrame,id_col: str = "id")->Tuple[pd.DataFrame,pd.DataFrame]:
        """Splits data into train and test sets"""
        try:
            test_ratio = self.data_ingestion_config.train_test_split_ratio
            ids = df[id_col]
            in_test_set = ids.apply(lambda id_: crc32(np.int64(id_)) & 0xffffffff < test_ratio * 2**32)
            return df.loc[~in_test_set].drop(columns=[id_col]),df.loc[in_test_set].drop(columns=[id_col])
        except Exception as e:
            raise CustomException(e,sys)
    
    @abstractmethod
    def close(self):
        pass


