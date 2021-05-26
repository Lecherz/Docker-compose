from flask import Flask, jsonify
from flask import request
import pymongo
import json
import sys
import database1



#database part
app = Flask(__name__)
db_add = "mongodb2://192.168.199.128:27018/"


@app.route('/', methods=['GET'])
def query_point():
    data1 = database1.main(db_add)
    return jsonify(data1)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)




