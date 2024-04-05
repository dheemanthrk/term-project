import json
import boto3

dynamodb = boto3.resource('dynamodb')
quiz_table = dynamodb.Table('YourQuizTableName')

def lambda_handler(event, context):
    try:
        # Extract quiz set ID from the request
        quiz_set_id = event['queryStringParameters']['quizSetId']
        
        # Retrieve quiz questions for the given quiz set ID from DynamoDB
        response = quiz_table.get_item(
            Key={
                'QuizSetID': quiz_set_id
            }
        )
        
        # Check if the quiz set exists
        if 'Item' not in response:
            return {
                'statusCode': 404,
                'body': json.dumps({'message': 'Quiz set not found'})
            }
        
        # Extract quiz questions from the response
        quiz_questions = response['Item']['QuizQuestions']
        
        # Return the quiz questions
        return {
            'statusCode': 200,
            'body': json.dumps(quiz_questions)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': str(e)})
        }
