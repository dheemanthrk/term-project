import json
import boto3

def create_quiz_set(event, context):
    # Parse the incoming request
    request_body = json.loads(event['body'])
    quiz_set_id = request_body['quiz_set_id']
    questions = request_body['questions']
    options = request_body['options']
    correct_answers = request_body['correct_answers']

    # Validate the input data
    if not quiz_set_id or not questions or not options or not correct_answers:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Missing required fields'})
        }

    # Connect to DynamoDB
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('QuizSets')

    # Insert the new quiz set into DynamoDB
    try:
        table.put_item(Item={
            'quiz_set_id': quiz_set_id,
            'questions': questions,
            'options': options,
            'correct_answers': correct_answers
        })
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Failed to create quiz set', 'error': str(e)})
        }

    # Return success response
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Quiz set created successfully'})
    }
