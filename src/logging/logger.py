# General imports
from typing import Literal
from logging.handlers import RotatingFileHandler
from logging import StreamHandler,Formatter,Logger,INFO

# Package imports
from .settings import LoggerSettings

def get_logger(name: str,level: Literal[20]=INFO)->Logger:
    """Function for creating a logger object"""

    logger_settings = LoggerSettings() # Fetches logger settings

    logger = Logger(name=name) # Creates a logger
    logger.setLevel(level=level) # Sets logger level

    formatter = Formatter(
        fmt=logger_settings.FORMAT,
        datefmt=logger_settings.DATE_FORMAT
    ) # Creates a formatter

    stream_handler = StreamHandler() # Creates a stream handler
    stream_handler.setLevel(level) # Sets stream handler level
    stream_handler.setFormatter(formatter) # Sets stream handler formatter

    file_path = logger_settings.BASE_FOLDER_PATH/logger_settings.LOGS_FOLDER_NAME # Specifies the file path
    file_path.mkdir(exist_ok=True,parents=True) # Creates the file path if it doesn't exist

    file_handler = RotatingFileHandler(
        filename=logger_settings.BASE_FOLDER_PATH/logger_settings.LOGS_FOLDER_NAME/f"{name}.log",
        maxBytes=logger_settings.FILE_HANDLER_MAX_BYTES,
        backupCount=logger_settings.FILE_HANDLER_BACKUP_COUNT
    ) # Creates a file handler
    file_handler.setLevel(level) # Sets file handler level
    file_handler.setFormatter(formatter) # Sets file handler formatter

    logger.addHandler(stream_handler) # Adds stream handler to logger
    logger.addHandler(file_handler) # Adds file handler to logger

    return logger