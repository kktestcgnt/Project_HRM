import pymongo

'''
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
'''


# How to pass MongoDB database/collection name as a parameter
def mongo(db_name='mydb', col_name='sysusers'):
    uri = "mongodb://192.168.29.72:27017/"
    mongo_client = pymongo.MongoClient(uri)
    print(mongo_client)
    print("Connection is Successful")

    print("DBs in Mongo DB client: ", mongo_client.list_database_names())

    # Connect to an existing Database
    # data_db = mongo_client.mydb

    # List all the collection names
    # print("Collections in required DB: ", data_db.list_collection_names())

    # mongo_client[db_name][col_name].insertMany([{'userrole': 'Admin', 'status': 'Enabled', 'empname': 'emp2', 'username': 'user2'}, {'userrole': 'Admin', 'status': 'Enabled', 'empname': 'emp3', 'username': 'user3'}])

    print(type(mongo_client[db_name]))
    req_db_collection = mongo_client[db_name][col_name]
    # req_mongo_data = None
    print("find check : ", req_db_collection.find())
    count = 0
    for mongo_doc in req_db_collection.find():
        count = count + 1
        print(req_db_collection.find())
        req_mongo_data = mongo_doc
        print(req_mongo_data)
        print(count)


mongo()
