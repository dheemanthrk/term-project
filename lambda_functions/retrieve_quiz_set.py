import json
import boto3

def retrieve_quiz_set(event, context):
    # Parse the incoming request to extract the quiz set ID
    quiz_set_id = event['queryStringParameters']['quiz_set_id']

    # Connect to DynamoDB
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('QuizSets')

    # Retrieve the quiz set from DynamoDB
    try:
        response = table.get_item(Key={'quiz_set_id': quiz_set_id})
        quiz_set = response.get('Item')
        if not quiz_set:
            return {
                'statusCode': 404,
                'body': json.dumps({'message': 'Quiz set not found'})
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Failed to retrieve quiz set', 'error': str(e)})
        }

    # Return the retrieved quiz set
    return {
        'statusCode': 200,
        'body': json.dumps(quiz_set)
    }
