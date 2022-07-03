import os
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient


MONGO_DB_URL = os.environ.get('MONGO_DB_URL')



mongo = MongoClient(MONGO_DB_URL)
db = mongo.LGMT
YashviLovesAlpha = db


