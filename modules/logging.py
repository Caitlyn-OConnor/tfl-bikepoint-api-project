import logging
import os
from datetime import datetime

def logging_function(prefix, timestamp):
    '''
    Setting up logging
    
    :param prefix: for the folder name of the logs
    :param timestamp: for the name of the log files
    '''
    #making logging dir if it doesnt already exist with the desired prefix
    dir = f'{prefix}_logs'
    os.makedirs(dir, exist_ok=True)

    #making log file name with timestamp of main.py runtime
    log_filename = f"{dir}/{timestamp}.log"

    # configured log files
    logging.basicConfig(
        level=logging.INFO, 
        format='%(asctime)s - %(levelname)s - %(message)s',
        filename=log_filename
    )   

    return logging.getLogger(prefix)