import boto3
import json

# Connect to DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('processed_reviews')

# Connect to S3
s3 = boto3.client('s3')
bucket_name = 'productreview-pipeline'
prefix = 'processed-reviews/'

# List JSON files in the S3 prefix
response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)

for obj in response.get('Contents', []):
    key = obj['Key']
    
    if key.endswith(".json"):
        s3_response = s3.get_object(Bucket=bucket_name, Key=key)
        content = s3_response['Body'].read().decode('utf-8')

        for line in content.strip().splitlines():
            item = json.loads(line)
            table.put_item(
                Item={
                    'review_id': item['review_id'],
                    'review': item['review'],
                    'sentiment': item['sentiment']
                }
            )

print("All reviews successfully uploaded to DynamoDB.")
