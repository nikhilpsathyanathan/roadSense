from flask import Flask
import pymongo


app = Flask(__name__)
@app.route('/')
def index():
 return 'Hello world'

@app.route('/<name>')
def hello_name(name):
   return 'Hello %s!' % name

if __name__ == '__main__':
 app.run(host='127.0.0.1', debug=True, port=8080)
