from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
import json
import os
import requests

application = Flask(__name__)

application.config["MONGO_URI"] = 'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + \
     os.environ['MONGODB_PASSWORD'] + '@' + os.environ['MONGODB_HOSTNAME'] + ':27017/' + \
         os.environ['MONGODB_DATABASE']

mongo = PyMongo(application)
db = mongo.db
coll = db.parsed

@application.route('/')
def hello():
    return "Hello From  Client"

@application.route('/parse', methods=['POST'])
def extract():
    text = request.get_json()['text']
    payload = json.dumps({
        "text":text
    })
    headers = {
        'Content-type' : 'applications/json'
    }
    response = requests.request("POST", url="http://localhost:5055/model/parse", \
        headers=headers, data=payload)
    
    return response.json()


if __name__ == "__main__":
    application.run(host = '0.0.0.0', debug=True, port=5056, use_reloader=True)