import requests
from bson.json_util import loads
import json

IP = 'http://localhost:8000/'


def get():
    response = requests.get(IP)
    return response.json()


def post(body):
    data = {'Disease': body}
    data=json.dumps(data)
    response = requests.post(IP + 'post', data)
    response=response.json()
    print("dfkldf;gksdf;sfdshfsfgh",response)
    return response


