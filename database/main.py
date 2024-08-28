"""
Hand using Mongo
"""

from database.engine import MongoDBEngine


def print_all_data():
    """For visualisate"""
    mongo = MongoDBEngine()
    db_client = mongo.create_client()
    db = db_client[mongo.get_db_name()]
    collections = db.list_collection_names()

    for collection_name in collections:
        collection = db[collection_name]
        print(f"\nDocuments in collection '{collection_name}':")
        for document in collection.find():
            print(document)


if __name__ == "__main__":
    print_all_data()
