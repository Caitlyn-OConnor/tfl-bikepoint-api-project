import boto3
import os

def load_function(data_dir, AWS_ACCESS_KEY, AWS_SECRET_KEY, bucket_name, logger):
    '''
    Loads json files into an s3 bucket 
    
    :param data_dir: where the extracted data lives
    :param access_key: s3 access key
    :param secret_key: s3 secret access key
    :param bucket_name: name of s3 bucket
    :param logger: name of logger
    '''
    s3_client = boto3.client(
    's3', 
    aws_access_key_id = AWS_ACCESS_KEY, 
    aws_secret_access_key = AWS_SECRET_KEY
    )

    # 1. Get a list of only the .json files
    json_files = [f for f in os.listdir(data_dir) if f.endswith('.json')]

    # 2. Use the list for your if/else logic
    if json_files:
        print(f"Found {len(json_files)} files. Starting upload...")
        
        for file in json_files:
            local_file_path = os.path.join(data_dir, file)
            try:
                # Upload to S3
                s3_client.upload_file(local_file_path, bucket_name, file)
                
                # Delete local file AFTER successful upload
                os.remove(local_file_path) 
                print(f'Successfully uploaded and removed {file} :)')
                logger.info(f'{file} uploaded successfully :)')  

            except Exception as e:
                print(f'Upload error for {file}: {e}')
                logger.error(f'An error occurred on upload {e}')  
                  
    else:
        # This runs if json_files is empty
        print('No JSON files found in the directory. Nothing to upload.')
