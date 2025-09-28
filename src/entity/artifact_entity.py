# Imports
from pathlib import Path
from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    """Class for data ingestion artifacts"""
    ingested_train_file_path:Path
    ingested_test_file_path:Path