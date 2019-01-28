from django.shortcuts import render
from django.http import HttpResponse
from bson.json_util import dumps,loads
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from pymongo import MongoClient
Client = MongoClient ()
db = Client['Diebrary']
Collection = db['Diseases']


def get (request):
        x = Collection.find()
        b=HttpResponse (dumps(x))
        b["Content-Type"] = "application/json"
        print(b)
        return b


def post (request):
        disease = loads(request.body)
        c = Collection.find(disease)
        # print("Request",loads(request.body)['Disease'])
        # c = Collection.find({'Disease':loads(request.body)['Disease']["Disease"]})
        change=HttpResponse(dumps(c))
        change["Content-Type"] = "application/json"
        print (change)
        return change
        # return HttpResponse("Chicken")
def put ():
    pass

