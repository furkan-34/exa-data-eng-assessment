import json
import os
import pandas as pd
from pymongo import MongoClient

path = "data"
client = MongoClient("<mongodb-connection-string>")
db = client['emis']

for file in os.listdir(path):
    print(f"Uploading for {file}")
    df = pd.read_json(f"{path}/{file}")
    records = json.loads(df.T.to_json()).values()

    collection = db[file]
    collection.insert_many(records)
