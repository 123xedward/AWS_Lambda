import boto3
import time

client = boto3.client('iam')

#1 Create the user
response = client.create_user(
    UserName='123xedward', #mandatory
    PermissionsBoundary='arn:aws:iam::aws:policy/AmazonEC2ReadOnlyAccess' #ARN of policy
)
print(response)
time.sleep(15)

#Optional, add user to existing role
response = client.add_user_to_group(
    GroupName='AdminGroup',
    UserName='123xedward'
)
print(response)
time.sleep(15)

#Create the credentials for user
response = client.create_access_key(
    UserName='123xedward' #return access key and secret access key
)
print(response)
time.sleep(15)