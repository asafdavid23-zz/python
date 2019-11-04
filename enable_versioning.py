#!/usr/bin/python3
import boto3

client = boto3.client('s3')

for bucket in client.list_buckets()['Buckets']:
    response = client.get_bucket_versioning(
    Bucket=bucket['Name']
    )
    if (response['Status'] == 'Enabled'):
        print('Versioning is Already Enabled on %s.' % bucket['Name'])
    elif (response['Status'] != 'Enabled'):
        client.put_bucket_versioning(
            Bucket=bucket['Name'],
            VersioningConfiguration={
                'MFADelete': 'Disabled',
                'Status': 'Enabled'
            }
        )
        print('%s is Done.' % bucket['Name'])