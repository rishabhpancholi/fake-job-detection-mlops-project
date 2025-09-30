# General Imports
import sys
import numpy as np
import pandas as pd
from zlib import crc32
from typing import Tuple
from abc import ABC,abstractmethod

# Package imports
from src.exception import CustomException
from src.config import TrainingPipelineConfig,DataIngestionConfig

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

    @staticmethod
    def clean_data(df: pd.DataFrame)->pd.DataFrame:
        """Cleans the data"""
        try:
            return (
                        df
                        .assign(
                            text = lambda df:(
                                df[['title',
                                    'location','department',
                                    'company_profile','description',
                                    'requirements','benefits',
                                    'industry','function']]
                                .fillna('')
                                .agg(''.join, axis=1)
                            )
                            .str.replace(r'[,.!:;]','',regex = True)
                            .str.replace(r'([a-z])([A-Z])',r'\1 \2',regex = True)
                            .str.replace(r'[()]','',regex = True)
                        )
                        .drop(columns = [
                                        'title',
                                        'location',
                                        'department',
                                        'company_profile',
                                        'description',
                                        'requirements',
                                        'benefits',
                                        'industry',
                                        'function'
                                        ])
        )
        except Exception as e:
            raise CustomException(e,sys)

    def split_data(self,df: pd.DataFrame,id_col: str = "job_id")->Tuple[pd.DataFrame,pd.DataFrame]:
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


