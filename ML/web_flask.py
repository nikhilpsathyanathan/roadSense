from flask import Flask, render_template
import pymongo
import os 
#os.system('python main.py')

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["local"]
mycol = mydb["data"]

app = Flask(__name__)
@app.route('/')
def index():
 return render_template('index.html')

@app.route('/<name>')
def hello_name(name):
   return 'Hello %s!' % name

if __name__ == '__main__':
 app.run(host='127.0.0.1', port=5000)
