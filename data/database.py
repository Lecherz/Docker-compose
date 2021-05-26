import pymongo

myclient = pymongo.MongoClient("mongodb://192.168.199.128:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["key"]

def insert_db(message):
    my_dict = {"message": message}
    x = mycol.insert_one(my_dict)
    return x.inserted_id
