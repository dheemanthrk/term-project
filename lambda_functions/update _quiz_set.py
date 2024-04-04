import json
import boto3

def update_quiz_set(event, context):
    # Parse the incoming request to extract the quiz set details
    request_body = json.loads(event['body'])
    quiz_set_id = request_body['quiz_set_id']
    updated_questions = request_body['questions']

    # Connect to DynamoDB
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('QuizSets')

    # Update the quiz set in DynamoDB
    try:
        response = table.update_item(
            Key={'quiz_set_id': quiz_set_id},
            UpdateExpression="set questions = :q",
            ExpressionAttributeValues={':q': updated_questions},
            ReturnValues="UPDATED_NEW"
        )
        updated_quiz_set = response.get('Attributes')
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Failed to update quiz set', 'error': str(e)})
        }

    # Return the updated quiz set
    return {
        'statusCode': 200,
        'body': json.dumps(updated_quiz_set)
    }
