import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://MongoUser:Password1@clusterdb.ekaau.mongodb.net/?retryWrites=true&w=majority")

db = cluster["CyberClass"]
collection = db["PhoneBook"]

data1 = {"name":"noya","phone": "054755654807","hairstyle":"curly"}
try:

    collection.insert_one(data1)

except:
    print("already exists")
