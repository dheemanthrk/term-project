import json
import boto3

# Create an instance of DynamoDB client
dynamodb = boto3.client('dynamodb')

# Lambda handler function
def lambda_handler(event, context):
    try:
        params = {
            'TableName': 'QuizData',
            'KeyConditionExpression': 'ID = :id',
            'ExpressionAttributeValues': {
                ':id': {'S': '1'}  # Replace '1' with the actual ID value you want to retrieve
            }
        }
        # Query DynamoDB to retrieve all quiz questions
        response = dynamodb.query(**params)

        # Extract quiz questions from the response
        quiz_questions = []
        for item in response.get("Items", []):
            question = {
                "ID": item.get("ID", {}).get("S"),
                "QuestionID": item.get("QuestionID", {}).get("S"),
                "QuestionText": item.get("QuestionText", {}).get("S"),
                "Options": [option.get("S") for option in item.get("Options", {}).get("M", {}).values()],
                "CorrectAnswer": item.get("CorrectAnswer", {}).get("S")
                }
            quiz_questions.append(question)

        # Prepare the response
        return {
            'statusCode': 200,
            'body': json.dumps(quiz_questions)
        }
    except Exception as e:
        print('Error fetching quiz questions:', e)
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Failed to fetch quiz questions'})
        }
