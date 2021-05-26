import pymongo
import json

def db_all(mycol):
    db_list = []
    for x in mycol.find():
        data = str(x).replace("ObjectID(","")
        data = data.replace(")","")
        data = data.replace("","")
        data = data.replace('"data":"{','')
        data = data.replace('}"','')
        db_list.append(json.loads(data))
    return db_list
def main(db_add):
    db_add = "mongodb2://192.168.199.128:27018/"
    myclient = pymongo.MongoClient(db_add)
    mydb = myclient["mydatabase2"]
    mycol = mydb["key"]
    return db_all(mycol)

