import boto3
import json
import base64
import uuid

s3 = boto3.client('s3')
bucket_name = 'productreview-pipeline'

def lambda_handler(event, context):
    for record in event['Records']:
        payload = base64.b64decode(record['kinesis']['data'])
        review_data = json.loads(payload)

        review_id = str(uuid.uuid4())
        review_data['review_id'] = review_id

        s3.put_object(
            Bucket=bucket_name,
            Key=f"raw-reviews/{review_id}.json",
            Body=json.dumps(review_data)
        )

    return {
        'statusCode': 200,
        'body': 'Saved to S3'
    }
