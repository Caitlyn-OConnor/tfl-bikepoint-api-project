# importing packages
import requests
import os
from datetime import datetime
import json
import time
import logging

# logging directory name 
logs_dir = 'logs'

# making sure the log directory exists before creating one
if os.path.exists(logs_dir):
    pass
else:
    os.mkdir(logs_dir)

# creating the filename variables to be referenced later
filename = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
log_filename = f"logs/{filename}.log"

# configured log files
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename=log_filename
)

# creating logger variable
logger = logging.getLogger()

# Documentation here https://api.tfl.gov.uk/swagger/ui/#!/BikePoint/BikePoint_GetAll
url = 'https://api.tfl.gov.uk/BikePoint'

# creating attempt variables where max is 3
no_of_tries = 3
attempts = 0

while attempts < no_of_tries:
    # calling api 
    response = requests.get(url,timeout=10)
    status_code = response.status_code

    if status_code==200:
        # if successful, create json file in a directory called data
        response_json = response.json()

        dir = 'data'

        # making the directory if it doesnt already exist
        if os.path.exists(dir):
            pass
        else:
            os.mkdir(dir)

        filepath = f'{dir}/{filename}.json'

        #will create json file or error if unsuccessful 
        try:
            with open(filepath,'w') as file:
                json.dump(response_json,file)
            print(f'Download successful at {filename} :)')
            logger.info(f'Download successful at {filename} :)')  
        except Exception as e:
            print(e)
            logger.error(f'An error occurred {e}')     
        break

    # if the api call error was my a system failure, then retry after 10s
    elif status_code>499 or status_code<200:
        print(response.reason)
        logger.warning(response.reason)       
        time.sleep(10)
        attempts+=1

    # if error by personal error then don't retry
    else:
        print(response.reason)
        logger.error(response.reason)  
        break

