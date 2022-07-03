
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient


import Config



mongo = MongoClient(config.MONGO_DB_URL)
db = mongo.LGMT



