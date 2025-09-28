# Imports
import sys

class CustomException(Exception):
    """Custom exception class for the project"""
    def __init__(self, error_message: Exception, error_detail:sys):
        super().__init__(str(error_message))
        self.error_message:str = str(error_message)
        self.error_detail:sys = error_detail
        _,_,exc_tb = self.error_detail.exc_info() # Extracts the traceback
        self.line_number:int = exc_tb.tb_lineno # Extracts the line number
        self.file_name:str = exc_tb.tb_frame.f_code.co_filename # Extracts the file name

    def get_detailed_message(self)->str:
        """Gets the detailed formatted error message"""
        detailed_message = f"Error occurred in script [{self.file_name}] at line number [{self.line_number}] with error message [{self.error_message}]" # Creates the detailed message
        return detailed_message
    
    def __str__(self)->str:
        """Returns the formatted error message"""
        return self.get_detailed_message() # Returns the detailed message
