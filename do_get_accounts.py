import json
from botocore.vendored import requests
import os


api_token = os.environ["ap_token"]
api_url_base = os.environ["api_url_base"]

headers = {'Content-Type': 'application/json',
           'TRN-Api-Key': (api_token)
           }

platform = 'xbox'
epic_name = 'mnj1222'

def acctinfo(event,context):
    api_url = '{}{}/{}'.format(api_url_base, platform, epic_name)
    response = requests.get(api_url, headers=headers)
    response_data = json.dumps(response)

    if response.status_code == 200:
        return {"isBase64Encoded": False,"statusCode": 200, "headers": {'content-type': 'application/json'}, "body": response.json}
        #return response_data
    else:
        return None

# account_info = acctinfo()
#
# if account_info is not None:
#     print("Here's your info: ")
#     for k, v in account_info.items():
#         print('{0}:{1}'.format(k, v))
#
# else:
#     print('[!] Request Failed')

# "body": json.loads(response.content.decode('utf-8'))}
