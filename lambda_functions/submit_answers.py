import json
import boto3

dynamodb = boto3.resource('dynamodb')
quiz_table = dynamodb.Table('YourQuizTableName')

def calculate_score(answers, correct_answers):
    score = 0
    for i in range(len(answers)):
        if answers[i] == correct_answers[i]:
            score += 1
    return score

def lambda_handler(event, context):
    try:
        # Extract quiz set ID and submitted answers from the request
        quiz_set_id = event['quizSetId']
        submitted_answers = event['answers']
        
        # Retrieve correct answers for the given quiz set ID from DynamoDB
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
        
        # Extract correct answers from the response
        correct_answers = response['Item']['CorrectAnswers']
        
        # Calculate the score
        score = calculate_score(submitted_answers, correct_answers)
        
        # Return the score
        return {
            'statusCode': 200,
            'body': json.dumps({'score': score})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': str(e)})
        }
