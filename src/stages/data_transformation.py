# General Imports
import sys
import spacy
import numpy as np
import pandas as pd
from pathlib import Path

# Package Imports
from src.constants import *
from src.utils import Utility
from src.logging import get_logger
from src.exception import CustomException

class DataTransformation:
    """Class for data transformation stage"""
    def __init__(self, logger = get_logger('data_transformation'), utils = Utility()):
        """Initializes the data transformation class"""
        try:
            self.ingested_train_file_path = Path(ARTIFACTS_DIR)/DATA_INGESTION_DIR_NAME/DATA_INGESTION_TRAIN_FILE_NAME
            self.ingested_test_file_path = Path(ARTIFACTS_DIR)/DATA_INGESTION_DIR_NAME/DATA_INGESTION_TEST_FILE_NAME
            self.transformed_train_file_path = Path(ARTIFACTS_DIR)/DATA_TRANSFORMATION_DIR_NAME/DATA_TRANSFORMATION_TRANSFORMED_TRAIN_FILE_NAME
            self.transformed_test_file_path = Path(ARTIFACTS_DIR)/DATA_TRANSFORMATION_DIR_NAME/DATA_TRANSFORMATION_TRANSFORMED_TEST_FILE_NAME
            self.nlp = spacy.load('en_core_web_sm',disable=['parser','ner','textcat'])
            self.utils = utils
            self.log = logger
            self.log.info("Data Transformation started")
        except Exception as e:
            raise CustomException(e,sys)
        
    def lemmatize_text(self,ser: pd.Series)-> pd.Series:
        """Lemmatizes the text"""
        try:
            self.log.info("Lemmatizing the text")
            texts = ser.to_list()
            clean_texts = []
            for doc in self.nlp.pipe(texts,batch_size = 64,n_process = -1):
                tokens = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
                clean_texts.append(' '.join(tokens))
            self.log.info("Text lemmatized successfully")
            return pd.Series(clean_texts)
        except Exception as e:
            raise CustomException(e,sys)
        
    def clean_data(self, df:pd.DataFrame)-> pd.DataFrame:
        """Cleans the data"""
        try:
            self.log.info("Cleaning the data")
            return (
                df
                .assign(
                    salary_range = lambda df:(
                        np.where(
                            df.salary_range.isnull(),
                            'Not Mentioned',
                            'Mentioned'
                        )
                    ),
                    text = lambda df:(
                        df[["title","location","department","company_profile","description","requirements","benefits","industry","function"]]
                        .fillna('')
                        .agg(''.join, axis=1)
                    )
                    .str.replace(r'[,.!:;]','',regex = True)
                    .str.replace(r'([a-z])([A-Z])',r'\1 \2',regex = True)
                    .str.replace(r'[()]','',regex = True)
                    .str.lower().str.replace(r'[^a-z\s]','',regex=True)
                    .pipe(self.lemmatize_text)     
                )
                .drop(columns = ["title","location","department","company_profile","description","requirements","benefits","industry","function"])
            )
        except Exception as e:
            raise CustomException(e,sys)
        
    def impute_data(self, df:pd.DataFrame)-> pd.DataFrame:
        """Imputes the data"""
        try:
            self.log.info("Imputing the data")
            col_list  = ["employment_type","required_experience","required_education"]
            return(
                    df.assign(
                    **{
                        col: df[col].fillna('Not Mentioned')
                        for col in col_list
                    }
                )
            )
        except Exception as e:
            raise CustomException(e,sys)
        
    def transform(self):
        """Transforms the data"""
        try:
            train_df = self.utils.load_data(self.ingested_train_file_path)
            test_df = self.utils.load_data(self.ingested_test_file_path)
            train_df = self.clean_data(train_df)
            test_df = self.clean_data(test_df)
            self.log.info("Data cleaned successfully")
            train_df = self.impute_data(train_df)
            test_df = self.impute_data(test_df)
            self.log.info("Data imputed successfully")
            self.log.info("Saving the transformed dataframes to csv files")
            self.utils.save_data(train_df,self.transformed_train_file_path)
            self.utils.save_data(test_df,self.transformed_test_file_path)
            self.log.info("Transformed dataframes saved successfully")
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__ == '__main__':
    data_transformation = DataTransformation()
    data_transformation.transform()

    
