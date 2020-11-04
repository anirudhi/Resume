import requests
import json
import sys


file_name = sys.argv[1]
files = {'resume': open(file_name, 'rb')}
# decode the resume from base64
#    resume = b64decode(body['content'])

# ask Lever to parse our resume
parseResponse = requests.post('https://jobs.lever.co/parseResume', files=files)

# return a response for API gateway
response = {
    "statusCode": 200,
    "headers": {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "https://itsjafer.com",
        "Access-Control-Allow-Headers" : "Content-Type",
        "Access-Control-Allow-Methods": "POST"
    },
    "body": json.dumps(parseResponse.json())
};
print(response)
