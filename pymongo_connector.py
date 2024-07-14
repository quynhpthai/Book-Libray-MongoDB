# pip install pymongo
# pip install dnspython


import pymongo

dbname = "bookmanager"
collection_B = "Book"
collection_P="Publisher"
myclient = pymongo.MongoClient("mongodb://root:password@127.0.0.1:27017/")
# print(myclient.list_database_names())

mydb = myclient[dbname]

# Get a collection
collection_B = mydb[collection_B]
collection_P=mydb[collection_P]

