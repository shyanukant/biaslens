from pymongo import MongoClient
from datetime import datetime
# from dataset import get_dataset

from dotenv import load_dotenv
import os

load_dotenv()  # Loads .env variables

MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb://localhost:27017/")

# MongoDB setup
mongo_client = MongoClient(MONGODB_URI)
db = mongo_client["biaslens"]
collection = db["articles"]

print("Connected to MongoDB", collection.name)

# BigQuery query
# results = get_dataset()

# Insert into MongoDB
# for row in results:
#     doc = {
#         "date": row.DATE.strftime("%Y-%m-%d"),
#         "source": row.SourceCommonName,
#         "url": row.DocumentIdentifier,
#         "themes": row.V2Themes,
#         "tone": row.V2Tone,
#         "locations": row.V2Locations,
#         "fetched_at": datetime.utcnow()
#     }
#     collection.insert_one(doc)