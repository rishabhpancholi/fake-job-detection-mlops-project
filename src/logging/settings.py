# Imports
from pathlib import Path
from dataclasses import dataclass
from get_project_root import root_path

@dataclass
class LoggerSettings:
    """Class for logger settings"""
    LOGS_FOLDER_NAME="logs"
    FILE_HANDLER_BACKUP_COUNT=5
    DATE_FORMAT="%Y-%m-%d %H:%M:%S"
    FILE_HANDLER_MAX_BYTES=5*1024*1024
    BASE_FOLDER_PATH=Path(root_path(ignore_cwd=False))
    FORMAT="%(asctime)s | %(name)s | %(levelname)s | %(message)s"