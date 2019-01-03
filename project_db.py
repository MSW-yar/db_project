from pymongo import MongoClient
from bson.json_util import dumps

# input regarding te diesase

disease = input ('What is your Disease?')
disease_d = {'disease':disease}
   
Client = MongoClient ()
db = Client['Diebrary']
Collection = db['Diseases']

def connection(disease): 
    Collection.insert_one(disease)
connection(disease_d)


x = Collection.find()
print (dumps(x))


