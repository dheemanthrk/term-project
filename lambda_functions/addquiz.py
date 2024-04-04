import json
import boto3

dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
    try:
        # Parse the JSON payload from the event
        quiz_question = json.loads(event['body'])
        
        # Add the quiz question to DynamoDB
        dynamodb.put_item(
            TableName='QuizQuestions',
            Item={
                'questionId': {'S': quiz_question['questionId']},
                'questionText': {'S': quiz_question['questionText']},
                'options': {'L': [{'S': option} for option in quiz_question['options']]},
                'correctAnswer': {'S': quiz_question['correctAnswer']}
            }
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Quiz question added successfully'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Error adding quiz question'})
        }
