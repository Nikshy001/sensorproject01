from pymongo.mongo_client import MongoClient
import pandas as pd
import json

#url = 
uri="mongodb+srv://pwskills:pwskills@cluster0.o7vls.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# create a new client and connect to server
client = MongoClient(uri)
# create a database name and collection name 
DATABASE_NAME ="pwskills"
COLLECTION_NAME = "waferfault"

df = pd.read_csv("C:\Users\DELL\OneDrive\Desktop\Sensor project\notebooks\wafer_23012020_041211.csv")
df.head()
df = df.drop("Unnamed: 0",axis=1)
df
json_record = list(json.loads(df.T.to_json()).values())
json_record
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)

