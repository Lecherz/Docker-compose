from flask import Flask, jsonify
from flask import request
import os
import publisher 
import pymongo
import json
import sys


#Flask Part
app = Flask(__name__)
data = {"key":"this is default"}

#database part
myclient = pymongo.MongoClient("mongodb://192.168.199.128:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["key"]


@app.route('/post_helloworld', methods=['POST','GET'])
def post_hello_world():
    data = request.get_json()
    token = publisher.publisher(data['key'])
    return {"message" : "completed "+token}


@app.route('/getdb', methods=['GET'])
def get_db():
    return jsonify(db_all())

def db_all():
    db_list = []
    for x in mycol.find():
        data = str(x).replace("ObjectId(","")
        data = data.replace(")","")
        data = data.replace("'",'"')
        db_list.append(json.loads(data))

    return db_list


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
