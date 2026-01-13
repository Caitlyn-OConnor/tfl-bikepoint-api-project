import boto3
from dotenv import load_dotenv
import os

load_dotenv()

AWS_ACCESS_KEY = os.getenv('AWS-ACCESS-KEY')
AWS_SECRET_KEY = os.getenv('AWS-SECRET-KEY')
BUCKET_NAME = os.getenv('BUCKET-NAME')
filepath = 'data'

s3_client = boto3.client(
    's3', 
    aws_access_key_id = AWS_ACCESS_KEY, 
    aws_secret_access_key = AWS_SECRET_KEY
)

# 1. Get a list of only the .json files
json_files = [f for f in os.listdir(filepath) if f.endswith('.json')]

# 2. Use the list for your if/else logic
if json_files:
    print(f"Found {len(json_files)} files. Starting upload...")
    
    for file in json_files:
        local_file_path = os.path.join(filepath, file)
        
        try:
            # Upload to S3
            s3_client.upload_file(local_file_path, BUCKET_NAME, file)
            
            # Delete local file AFTER successful upload
            os.remove(local_file_path) 
            print(f'Successfully uploaded and removed {file} :)')

        except Exception as e:
            print(f'Upload error for {file}: {e}')
else:
    # This runs if json_files is empty
    print('No JSON files found in the directory. Nothing to upload.')
