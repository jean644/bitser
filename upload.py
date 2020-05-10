import logging
import boto3
import os
from botocore.exceptions import ClientError
from configparser import ConfigParser

def upload(fileName):
    #Read config.ini file
    config_object = ConfigParser()
    config_object.read("config.ini")
    #Get the key and secret
    awsDetails = config_object["aws"]
    os.environ["AWS_ACCESS_KEY_ID"] = awsDetails["key"]
    os.environ["AWS_SECRET_ACCESS_KEY"] = awsDetails["secret"]
    
    
    
    
    # Let's use Amazon S3
    s3 = boto3.resource('s3')

    print ('Attempting to upload...')
    # Upload a new file
    data = open(fileName, 'rb')
    s3.Bucket('mmvm-1').put_object(Key=fileName, Body=data)
    print ('Uploaded')

#upload ('output.jpeg')