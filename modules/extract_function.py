import os
import json
import requests
import time

def extract_function(url, no_of_tries, logger, timestamp):
    '''
    Extracting jsons from the tfl bikepoint api
    
    :param url: url used for the api
    :param number_of_tries: max no of tries to call the api
    :param logger: name of logger dir 
    :param timestamp: time of main py run
    '''
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

            filepath = f'{dir}/{timestamp}.json'

            #will create json file or error if unsuccessful 
            try:
                with open(filepath,'w') as file:
                    json.dump(response_json,file)
                print(f'Download successful at {timestamp} :)')
                logger.info(f'Download successful at {timestamp} :)')  
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

