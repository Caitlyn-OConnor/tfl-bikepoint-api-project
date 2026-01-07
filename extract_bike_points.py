import requests
import os
from datetime import datetime
import json
import time
import logging

logs_dir = 'logs'

# making sure the log directory exists before creating one
if os.path.exists(logs_dir):
    pass
else:
    os.mkdir(logs_dir)

filename = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
log_filename = f"logs/{filename}.log"

logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename=log_filename
)

logger = logging.getLogger()

# Documentation here https://api.tfl.gov.uk/swagger/ui/#!/BikePoint/BikePoint_GetAll
url = 'https://api.tfl.gov.uk/BikePoint'

no_of_tries = 3
attempts = 0

while attempts < no_of_tries:

    response = requests.get(url,timeout=10)
    status_code = response.status_code

    if status_code==200:
        response_json = response.json()

        dir = 'data'

        # making sure the directory exists before creating one
        if os.path.exists(dir):
            pass
        else:
            os.mkdir(dir)

        filepath = f'{dir}/{filename}.json'

        try:
            with open(filepath,'w') as file:
                json.dump(response_json,file)
            print(f'Download successful at {filename} :)')
            logger.info(f'Download successful at {filename} :)')  
        except Exception as e:
            print(e)
            logger.error(f'An error occurred {e}')     
        break

    elif status_code>499 or status_code<200:
        print(response.reason)
        logger.warning(response.reason)       
        time.sleep(10)
        attempts+=1

    else:
        print(response.reason)
        logger.error(response.reason)  
        break

