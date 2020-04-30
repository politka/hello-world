import pymongo

MONGO_HOST = "10.1.0.90"
MONGO_PORT = 25
MONGO_DB = "db_name"
MONGO_USER = "username"
MONGO_PASS = "fee3fa69-d0db-4efe-83713d24d65cb555"

con = pymongo.MongoClient(MONGO_HOST, MONGO_PORT)
db = con[MONGO_DB]
db.authenticate(MONGO_USER, MONGO_PASS)

print(db)

