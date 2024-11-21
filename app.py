import json
import boto3

code_pipeline = boto3.client('codepipeline')

def lambda_handler(event, context):
    try:
        print(f"event: {event}")
        job_id = event['CodePipeline.job']['id']
        
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
        
        # CodePipeline에 성공 결과 전송
        code_pipeline.put_job_success_result(jobId=job_id)
        
        return response
        
    except Exception as e:
        print(f"Error: {str(e)}")
        if 'job_id' in locals():
            code_pipeline.put_job_failure_result(
                jobId=job_id,
                failureDetails={
                    'type': 'JobFailed',
                    'message': str(e)
                }
            )
        raise e