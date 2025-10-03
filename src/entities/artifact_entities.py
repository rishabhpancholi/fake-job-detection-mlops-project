# Imports
from pathlib import Path
from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    train_file_path: Path
    test_file_path: Path