"""
Tests for database
"""

import unittest
from database.engine import MongoDBEngine


class TestMongo(unittest.TestCase):
    """
    Testing MongoDB works
    """

    def test_check_connection(self) -> bool:
        """
        Checking connection to MongoDB
        """
        for _ in range(5):
            client = MongoDBEngine().create_client()
            client.admin.command("ping")


if __name__ == "__main__":
    unittest.main()

