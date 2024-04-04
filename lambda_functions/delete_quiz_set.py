import json
import boto3

def delete_quiz_set(event, context):
    # Parse the incoming request to extract the quiz set ID
    request_body = json.loads(event['body'])
    quiz_set_id = request_body['quiz_set_id']

    # Connect to DynamoDB
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('QuizSets')

    # Delete the quiz set from DynamoDB
    try:
        response = table.delete_item(
            Key={'quiz_set_id': quiz_set_id},
            ReturnValues="ALL_OLD"
        )
        deleted_quiz_set = response.get('Attributes')
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Failed to delete quiz set', 'error': str(e)})
        }

    # Return the deleted quiz set
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Quiz set deleted successfully', 'deleted_quiz_set': deleted_quiz_set})
    }
