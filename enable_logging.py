import boto3
from botocore.exceptions import ClientError

client = boto3.client('s3')
response = client.list_buckets()
s3_logging_target_bucket = input('Enter Target bucket for s3 Logging: ')

for bucket in response['Buckets']:
    loc = client.get_bucket_location(Bucket=bucket["Name"])
    if loc['LocationConstraint'] == None:
        client = boto3.client('s3', region_name='us-east-1')
        response = client.list_buckets()
        log = client.get_bucket_logging(Bucket=bucket["Name"])
        if 'LoggingEnabled' not in log:
            client.put_bucket_logging(
                Bucket=bucket['Name'],
                BucketLoggingStatus={
                    'LoggingEnabled': {
                        'TargetBucket': s3_logging_target_bucket,
                        'TargetPrefix': bucket['Name']
                    }
                }
            )
            print('Enable logging on Bucket =%s' % (bucket['Name']))
        else:
            print('Bucket =%s, Logging: %s' % (bucket['Name'], log['LoggingEnabled']))

    elif loc['LocationConstraint'] == 'eu-west-1':
        client = boto3.client('s3', region_name='eu-west-1')
        response = client.list_buckets()
        log = client.get_bucket_logging(Bucket=bucket["Name"])
        if 'LoggingEnabled' not in log:
            client.put_bucket_logging(
                Bucket=bucket['Name'],
                BucketLoggingStatus={
                    'LoggingEnabled': {
                        'TargetBucket': '911833893017-lpfs-s3-logs-us-east-1',
                        'TargetPrefix': bucket['Name']
                    }
                }
            )
            print('Enable logging on Bucket =%s' % (bucket['Name']))
        else:
            print('Bucket =%s, Logging: %s' % (bucket['Name'], log['LoggingEnabled']))

    elif loc['LocationConstraint'] == 'ap-southeast-2':
        client = boto3.client('s3', region_name='ap-southeast-2')
        response = client.list_buckets()
        log = client.get_bucket_logging(Bucket=bucket["Name"])
        if 'LoggingEnabled' not in log:
            client.put_bucket_logging(
                Bucket=bucket['Name'],
                BucketLoggingStatus={
                    'LoggingEnabled': {
                        'TargetBucket': '911833893017-lpfs-s3-logs-us-east-1',
                        'TargetPrefix': bucket['Name']
                    }
                }
            )
            print('Enable logging on Bucket =%s' % (bucket['Name']))
        else:
            print('Bucket =%s, Logging: %s' % (bucket['Name'], log['LoggingEnabled']))

    elif loc['LocationConstraint'] == 'us-east-2':
        client = boto3.client('s3', region_name='us-east-2')
        response = client.list_buckets()
        log = client.get_bucket_logging(Bucket=bucket["Name"])
        if 'LoggingEnabled' not in log:
            client.put_bucket_logging(
                Bucket=bucket['Name'],
                BucketLoggingStatus={
                    'LoggingEnabled': {
                        'TargetBucket': '911833893017-lpfs-s3-logs-us-east-1',
                        'TargetPrefix': bucket['Name']
                    }
                }
            )
            print('Enable logging on Bucket =%s' % (bucket['Name']))
        else:
            print('Bucket =%s, Logging: %s' % (bucket['Name'], log['LoggingEnabled']))

    elif loc['LocationConstraint'] == 'eu-west-2':
        client = boto3.client('s3', region_name='eu-west-2')
        response = client.list_buckets()
        log = client.get_bucket_logging(Bucket=bucket["Name"])
        if 'LoggingEnabled' not in log:
            client.put_bucket_logging(
                Bucket=bucket['Name'],
                BucketLoggingStatus={
                    'LoggingEnabled': {
                        'TargetBucket': '911833893017-lpfs-s3-logs-us-east-1',
                        'TargetPrefix': bucket['Name']
                    }
                }
            )
            print('Enable logging on Bucket =%s' % (bucket['Name']))
        else:
            print('Bucket =%s, Logging: %s' % (bucket['Name'], log['LoggingEnabled']))

    elif loc['LocationConstraint'] == 'eu-central-1':
        client = boto3.client('s3', region_name='eu-central-1')
        response = client.list_buckets()
        log = client.get_bucket_logging(Bucket=bucket["Name"])
        if 'LoggingEnabled' not in log:
            client.put_bucket_logging(
                Bucket=bucket['Name'],
                BucketLoggingStatus={
                    'LoggingEnabled': {
                        'TargetBucket': '911833893017-lpfs-s3-logs-eu-central-1',
                        'TargetPrefix': bucket['Name']
                    }
                }
            )
            print('Enable logging on Bucket =%s' % (bucket['Name']))
        else:
            print('Bucket =%s, Logging: %s' % (bucket['Name'], log['LoggingEnabled']))

