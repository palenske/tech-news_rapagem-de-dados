from pymongo import MongoClient
import copy

with open('connectionString.txt') as f:
    CONNECTION_STRING = f.readlines()

print(CONNECTION_STRING)

client = MongoClient(CONNECTION_STRING)
db = client.Tech_news


def create_news(data):
    db.news.insert_many(copy.deepcopy(data))


def insert_or_update(notice):
    return (
        db.news.update_one(
            {"url": notice["url"]}, {"$set": notice}, upsert=True
        ).upserted_id
        is not None
    )


def find_news():
    return list(db.news.find({}, {"_id": False}))


def search_news(query):
    return list(db.news.find(query))


def get_collection():
    return db.news
