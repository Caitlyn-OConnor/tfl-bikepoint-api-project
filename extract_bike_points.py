import requests
import os
from datetime import datetime
import json

# Documentation here https://api.tfl.gov.uk/swagger/ui/#!/BikePoint/BikePoint_GetAll
url = 'https://api.tfl.gov.uk/BikePoint'

response = requests.get(url,timeout=10)

response_json = response.json()

# print(response.status_code)
# print(response_json)

dir = 'data'

# making sure the directory exists before creating one
if os.path.exists(dir):
    pass
else:
    os.mkdir(dir)

filename = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
# print(filename)


filepath = f'{dir}/{filename}.json'
# print(filepath)

with open(filepath,'w') as file:
    json.dump(response_json,file)

print(f'Download successful at {filename} :)')