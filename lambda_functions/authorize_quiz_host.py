import json

# Hardcoded username and password for demonstration purposes
VALID_USERNAME = "admin"
VALID_PASSWORD = "password123"

def lambda_handler(event, context):
    # Parse the request body to extract username and password
    body = json.loads(event["body"])
    username = body.get("username")
    password = body.get("password")
    
    # Compare the provided username and password with the hardcoded values
    if username == VALID_USERNAME and password == VALID_PASSWORD:
        # Return an authentication token if they match
        response = {
            "statusCode": 200,
            "body": json.dumps({"message": "Authentication successful", "token": "your-auth-token"})
        }
    else:
        # Return a 401 Unauthorized status code if authentication fails
        response = {
            "statusCode": 401,
            "body": json.dumps({"message": "Authentication failed"})
        }
    
    return response
