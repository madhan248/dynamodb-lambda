import json
import datetime

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps(f'Hello from Lambda! {datetime.now()}')
    }
