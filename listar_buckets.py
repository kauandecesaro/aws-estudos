import boto3
import os
from dotenv import load_dotenv

load_dotenv()

aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
aws_region = os.getenv("AWS_REGION")

s3 = boto3.client(
    "s3",
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    region_name=aws_region
)

response = s3.list_buckets()
print("Buckets disponíveis:")
for bucket in response['Buckets']:
    print(f"- {bucket['Name']}")
