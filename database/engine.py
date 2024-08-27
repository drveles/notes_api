"""
Working with MongoDB in Docker container
"""

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure


class MongoDBEngine:
    __db_url = "mongodb://root:test@0.0.0.0/"
    __db_name = "Notes"
    __collection_name = "notes"

    def create_client(self) -> MongoClient:
        """
        Creating client to work with MongoDB
        """
        return MongoClient(
            self.__db_url,
            serverSelectionTimeoutMS=1000,
        )

    def get_db_name(self) -> str:
        """
        Getting database name
        """
        return self.__db_name

    def get_db_collection(self) -> str:
        """
        Getting database name
        """
        return self.__collection_name

    def check_connection(self) -> bool:
        """
        Checking connection to MongoDB
        """
        client = self.create_client()
        try:
            client.admin.command("ping")
            print("Successfully connected to MongoDB.")
        except ConnectionFailure as e:
            print("Could not connect to MongoDB: \n", e)


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
