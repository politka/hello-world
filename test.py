import pymongo




#GitGuardian test 
MONGO_HOST = "10.1.0.99"
MONGO_PORT = 25
MONGO_DB = "db_name"
MONGO_USER = "username"
MONGO_PASS = "fee3fa69-d0db-4efe-83713d24d65cb555"

MONGO_HOST = "bp.com"
MONGO_PORT = 25
MONGO_DB = "db_name"
MONGO_USER = "username"
MONGO_PASS = "fr3333f5-d0db-4efe-83713d24d65cb555"

from botocore.credentials import InstanceMetadataProvider, InstanceMetadataFetcher

provider = InstanceMetadataProvider(iam_role_fetcher=InstanceMetadataFetcher(timeout=1000, num_attempts=2))
credentials = provider.load()

access_key = "AKIAIOSFODNN7EXAMPLE"
secret_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

print access_key
print secret_key

con = pymongo.MongoClient(MONGO_HOST, MONGO_PORT)
db = con[MONGO_DB]
db.authenticate(MONGO_USER, MONGO_PASS)

print(db)

