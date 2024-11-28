import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://MongoUser:Password1@clusterdb.ekaau.mongodb.net/?retryWrites=true&w=majority")

db = cluster["CyberClass"]
collection = db["PhoneBook"]

data1 = {"name":"noya","phone": "054755654807","hairstyle":"curly"}
try:

    data = collection.find_one({"name":"noya"})
    print(type(data))
    print(data)
except:
    print("already exists")
