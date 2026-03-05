import json
import boto3
ACCESS_KEY = 'YOUR_ACCESS_KEY'
SECRET_KEY = 'YOUR_SECRET_KEY'
REGION_NAME = 'us-east-1' # Specify your region

client = boto3.client(
    's3',
    aws_access_key_id='AKIAQI5GDLR6V5NUMP2C',
    aws_secret_access_key='XLTIDvmfF8ZpxmGFw4zJB8sHj11xsGhcGEMkn+kl',
    region_name='ap-south-1'
)

sourcebucket = 'offline9-s3tos3-using-lambda'
destinationbucket = 'offline9-destination-bucket'

def copy_to_destination_bucket(filename):
    response = client.copy_object(Bucket='{}'.format(destinationbucket),CopySource='/{}/{}'.format(sourcebucket,filename),Key='{}'.format(filename))


def delete_from_source_bucket(filename):
    response = client.delete_object(Bucket='{}'.format(sourcebucket), Key='{}'.format(filename))


def main():
    print("*"*100)
    response = client.list_objects(Bucket='{}'.format(sourcebucket))
    for temp in response['Contents']:
        copy_to_destination_bucket(temp['Key'])
        delete_from_source_bucket(temp['Key'])
    print("*"*100)
    print("File successfully moved to Destionation bucket")

if __name__=='__main__':
    main()

