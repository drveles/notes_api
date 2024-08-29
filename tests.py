"""
Integration tests for API (clientside)
"""

import unittest
import asyncio
import aiohttp
import requests
from api import tests


class TestIntegrationAPIAsync(unittest.IsolatedAsyncioTestCase):
    """
    Async testing API works
    """

    test_counter = 10
    headers = {"Content-Type": "application/json"}
    __username1 = "test1"
    __sha_pass1 = "1b4f0e9851971998e732078544c96b36c3d01cedf7caa332359d6f1d83567014"

    async def test_available_route_add_note(self):
        """
        Testing conn to route `/add_note/`
        """
        async with aiohttp.ClientSession() as session:
            async with session.post("http://0.0.0.0:8000/add_note/") as response:
                self.assertLess(response.status, 500)

    async def test_available_route_notes(self):
        """
        Testing conn to route `/notes/`
        """
        async with aiohttp.ClientSession() as session:
            async with session.get("http://0.0.0.0:8000/notes/") as response:
                self.assertLess(response.status, 500)

    async def test_work_route_add_note(self):
        """
        Testing works route `/add_note/`
        """
        async with aiohttp.ClientSession() as session:
            json_body = {
                "note": "Test note ",
                "have_typo": False,
                "username": self.__username1,
                "sha_password": self.__sha_pass1,
            }

            for i in range(self.test_counter):
                json_body["note"] = json_body["note"] + str(i)
                async with session.post(
                    "http://0.0.0.0:8000/add-note/",
                    json=json_body,
                    headers=self.headers,
                ) as response:
                    self.assertLess(response.status, 300)

    async def test_correct_route_notes(self):
        """
        Testing works route `/notes/`
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(
                "http://0.0.0.0:8000/notes/",
                params={
                    "username": self.__username1,
                    "sha_password": self.__sha_pass1,
                },
                headers=self.headers,
            ) as response:
                self.assertLess(response.status, 300)


class TestIntegrationAPISync(unittest.TestCase):
    """
    Sync testing API works
    """

    headers = {"Content-Type": "application/json"}
    __username2 = "test2"
    __sha_pass2 = "60303ae22b998861bce3b28f33eec1be758a213c86c93c076dbe9f558c11c752"

    def test_available_route_add_note_sync(self):
        """
        Testing conn to route `/add_note/`
        """
        response =  requests.post("http://0.0.0.0:8000/add_note/") 
        self.assertLess(response.status_code, 500)

    def test_available_route_notes(self):
        """
        Testing conn to route `/notes/`
        """
        response = requests.get("http://0.0.0.0:8000/notes/")
        self.assertLess(response.status_code, 500)

    def test_work_route_add_note_sync(self):
        """
        Testing works route `/add_note/`
        """
        json_body = {
            "note": "Test note from requests",
            "have_typo": False,
            "username": self.__username2,
            "sha_password": self.__sha_pass2,
        }

        response = requests.post(
            "http://0.0.0.0:8000/add-note/",
            json=json_body,
            headers=self.headers,
        )
        self.assertLess(response.status_code, 300)


if __name__ == "__main__":
    suite_other = unittest.TestLoader().loadTestsFromModule(tests)
    suite_other.addTest(unittest.makeSuite(TestIntegrationAPIAsync))
    unittest.TextTestRunner(verbosity=2).run(suite_other)
    print()
    unittest.main()
