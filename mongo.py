import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["config"]

mycol = mydb["data"]

print(mydb.mycol.find( { $text: { $search: "10.60049944" } } ))
import json
from pprint import pprint

with open('temp.json') as data_file:    
    data = json.load(data_file)

x = mycol.insert_many(data)