import pymongo
import json

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["local"]
mycol = mydb["data"]
#mydict = {"lat": "10.1212","lon":"125223"}
#x = mycol.insert_one(mydict)

data_json = json.loads(data.to_json(orient='records'))
mycol.insert(data_json)