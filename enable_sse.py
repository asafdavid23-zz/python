#!/usr/bin/python3
import boto3
from botocore.exceptions import ClientError

client = boto3.client('s3', region_name='eu-west-1')

response = client.list_buckets()

for bucket in response['Buckets']:
    try:
        enc = client.get_bucket_encryption(Bucket=bucket['Name'])
        rules = enc['ServerSideEncryptionConfiguration']['Rules']
        print('Bucket =%s, Encryption: %s' % (bucket['Name'], rules))
    except ClientError as e:
        if e.response['Error']['Code'] == 'ServerSideEncryptionConfigurationNotFoundError':
            client.put_bucket_encryption(
            Bucket=bucket['Name'],
            ServerSideEncryptionConfiguration={
                'Rules': [
                    {
                        'ApplyServerSideEncryptionByDefault': {
                            'SSEAlgorithm': 'AES256'
                        }
                    },
                ]
            }
        )
            print('%s is Done.' % bucket['Name'])
        else:
            print("Bucket: %s, unexpected error: %s" % (bucket['Name'], e))