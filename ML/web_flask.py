from flask import Flask, render_template
import os 
from pymongo import MongoClient 
import pandas as pd
import numpy as np
import json
from flask import jsonify

app = Flask(__name__)
@app.route('/')
def index():
 return render_template('index.html')

@app.route('/<name>')
def hello_name(name):
   return 'Hello %s!' % name

@app.route('/getdata')
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
    return jsonify(jsonfiles)

if __name__ == '__main__':
 app.run(host='0.0.0.0', port=5000)
