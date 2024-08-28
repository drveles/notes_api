"""
Working with MongoDB in Docker container
"""

from pymongo import MongoClient


class MongoDBEngine:
    """
    Class to connection to MongoDB
    """

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
