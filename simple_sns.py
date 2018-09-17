import boto3
sns = boto3.client('sns')
phone_number = '52722XXXXXXX'
sns.publish(Message='Hello from CLI',PhoneNumber=phone_number)
