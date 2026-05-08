import boto3

s3_client = boto3.client('s3')
ec2_client = boto3.client('ec2')
ecs_client = boto3.client('ecs')
cloudwatchlogs_client = boto3.client('logs')