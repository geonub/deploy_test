import json

def lambda_handler(event, context):
    print(f"event: {event}")
    response = {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "message": "Hello, World!~~",
            "input": event
        })
    }
    
    return response
