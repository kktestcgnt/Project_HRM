import pymongo

uri = "mongodb://192.168.29.72:27017/"
mongo_client = pymongo.MongoClient(uri)
print(mongo_client)
print("Connection is Successful")

print("DBs in Mongo DB client: ", mongo_client.list_database_names())

# Connect to an existing Database
data_db = mongo_client.mydb

# List all the collection names
print("Collections in required DB: ", data_db.list_collection_names())

req_db_collection = data_db.sysusers
req_mongo_data = None
for mongo_doc in req_db_collection.find():
    req_mongo_data = mongo_doc
    print(req_mongo_data)
