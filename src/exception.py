# This allows you to handle runtime errors or exceptions that may occur during the execution of a program.
# By handling exceptions, you can prevent the program from crashing and provide a graceful way to handle errors.

import sys
import logging
from src.logger import logging

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info() # first two information I'm not interested and this will give on which line the error has occured
    file_name = exc_tb.tb_frame.f_code.co_filename #Custom exception
    error_message = "Error occured in python script namr [{0}] line number [{1}] error message[{2}]".format(
        file_name,exc_tb.tb_lineno,str(error))
        
    return error_message
    
    
class CustomException(Exception):
    '''
    This is a Python script that defines a custom exception class called CustomException. 
    1. The script imports the sys and logging modules for handling errors and logging messages.
    2. The error_massage_detail function takes two arguments: error, which is an instance of the Exception class, and error_detail, which is a sys object. 
    3. The function uses the exc_info() method of the error_detail object to retrieve the location and error message of the exception. 
    4. It then formats the error message into a string that includes the name of the script, the line number where the error occurred, and the error message itself. 
    5. Finally, the function returns the formatted error message.
    The CustomException class inherits from the built-in Exception class and adds a constructor that takes two arguments: error_message and error_detail. 
    The constructor calls the error_massage_detail function to generate a formatted error message and stores it in the error_message attribute of the CustomException instance. 
    The __str__ method of the class returns the error_message attribute as a string.
    This custom exception class can be used in Python scripts to handle errors in a more specific and informative way. When an instance of the CustomException class is raised, 
    it will contain a detailed error message that includes the location and message of the error. This can help developers to quickly identify and fix errors in their code.
    '''
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
    
    def __str__(self):
        return self.error_message
    
# checking if everthing is working or not
    
#if __name__ == "__main__":
        
    #try:
       # a = 1/0
            
    #except Exception as e:
       # logging.info("Zero Division Error")
        #raise CustomException(e,sys)