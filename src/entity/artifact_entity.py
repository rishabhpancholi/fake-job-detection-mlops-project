# Imports
from pathlib import Path
from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    ingested_train_file_path:Path
    ingested_test_file_path:Path