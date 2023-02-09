from pymongo import MongoClient
from datetime import datetime
#MONGODB QUERY BSON ENCODER ENGINE
import json
from bson import ObjectId
class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)
##### ENGINE END


def get_database(unitID):
    CONNECTION_STRING='mongodb+srv://test:test@onisoftdb.yvr8eto.mongodb.net/test'
    client = MongoClient(CONNECTION_STRING)
    return client[unitID]

def send_data(data,databasename):
    try: 
        dbname = get_database("onisoft") #nome da base de dados
        collectionname = dbname[databasename] #nome da coleção 
        collectionname.insert_one(data) #query

        

        return "ok"
    except:
        return "error 404"


def get_data(databasename):
    dbname = get_database('onisoft')
    collection = dbname[databasename]
    a = collection.find({"$query":{}})
    dataarr = [] 
    for i in a:
        dataarr.append(i)
    datauni = dataarr
    datafin = JSONEncoder().encode(datauni)
    return datafin

