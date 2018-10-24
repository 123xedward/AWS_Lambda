import boto3
import time

client = boto3.client('iam')

response = client.create_user(
    UserName='123xedward', #mandatory
    PermissionsBoundary='arn:aws:iam::aws:policy/AmazonEC2ReadOnlyAccess' #ARN of policy
)

