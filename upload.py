import logging
import boto3
from botocore.exceptions import ClientError

def upload(fileName):
    # Let's use Amazon S3
    s3 = boto3.resource('s3')

    print ('Attempting to upload...')
    # Upload a new file
    data = open(fileName, 'rb')
    s3.Bucket('mmvm-1').put_object(Key=fileName, Body=data)
    print ('Uploaded')
