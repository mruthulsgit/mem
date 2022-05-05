import pymongo
k="mongodb://localhost:27017/"
client=pymongo.MongoClient(k)
print(client.database_names())
