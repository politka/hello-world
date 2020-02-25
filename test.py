import pymongo

MONGO_HOST = "10.1.0.90"
MONGO_PORT = 25
MONGO_DB = "db_name"
MONGO_USER = "username"
MONGO_PASS = "password"

con = pymongo.MongoClient(MONGO_HOST, MONGO_PORT)
db = con[MONGO_DB]
db.authenticate(MONGO_USER, MONGO_PASS)

print(db)
