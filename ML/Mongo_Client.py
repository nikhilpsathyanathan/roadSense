from pymongo import MongoClient 
import pandas as pd
conn = MongoClient("mongodb://localhost:27017/")
import pandas as pd
import numpy as np
import json
mydb = conn["roadSense"]
mycol = mydb["map"]

def mongo_rec():
    conn = MongoClient('mongodb://127.0.0.1',27017)
    mydb = conn["roadSense"]
    mycol = mydb["map"]
    table = mycol.find()
    df =  pd.DataFrame(list(table))
    df=df.drop(['_id'], axis=1)
    df.drop(df.tail(1).index,inplace=True)
    print(df.head())
    jsonfiles = json.loads(df.to_json(orient='records'))
    print(jsonfiles)
    return jsonfiles

mongo_rec()    