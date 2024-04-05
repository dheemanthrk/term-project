import json
import boto3

dynamodb = boto3.resource('dynamodb')
score_table = dynamodb.Table('YourScoreTableName')

def lambda_handler(event, context):
    try:
        # Extract participant ID from the request
        participant_id = event['participantId']
        
        # Retrieve the score for the given participant ID from DynamoDB
        response = score_table.get_item(
            Key={
                'ParticipantID': participant_id
            }
        )
        
        # Check if the participant exists
        if 'Item' not in response:
            return {
                'statusCode': 404,
                'body': json.dumps({'message': 'Participant not found'})
            }
        
        # Extract the score from the response
        score = response['Item']['Score']
        
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
