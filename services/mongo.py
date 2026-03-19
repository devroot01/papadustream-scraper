from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()

class Mongo:
    def __init__(self):
        self.db=MongoClient(os.getenv("MONGO_URI"))[os.getenv("DB_NAME")]
    def save(self,data):
        self.db.content.update_one({"url":data["url"]},{"$set":data},upsert=True)
