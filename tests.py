"""
Integration tests for API (clientside)
"""

import unittest
import requests
from api import tests


class TestIntegrationAPISync(unittest.TestCase):
    """
    Sync testing API works
    """

    test_counter = 10
    headers = {"Content-Type": "application/json"}
    __username1 = "test1"
    __sha_pass1 = "1b4f0e9851971998e732078544c96b36c3d01cedf7caa332359d6f1d83567014"
    __username2 = "test2"
    __sha_pass2 = "60303ae22b998861bce3b28f33eec1be758a213c86c93c076dbe9f558c11c752"

    def test_available_route_add_note(self):
        """
        Testing conn to route `/add_note/`
        """
        response = requests.post("http://0.0.0.0:8000/add_note/")
        self.assertLess(response.status_code, 500)

    def test_available_route_notes(self):
        """
        Testing conn to route `/notes/`
        """
        response = requests.get("http://0.0.0.0:8000/notes/")
        self.assertLess(response.status_code, 500)

    def test_available_speller(self):
        """
        Testing conn to Yandex.Speller
        """
        response = requests.get(
            "https://speller.yandex.net/services/spellservice.json/checkText"
        )
        self.assertEqual(response.status_code, 200)

    def test_invalid_user(self):
        """
        Testing Auth
        """
        response = requests.get(
            "http://0.0.0.0:8000/notes/",
            params={"username": self.__username1, "sha_password": self.__sha_pass2},
        )
        self.assertGreater(response.status_code, 400)

    def test_add_note(self):
        """
        Testing works route `/add_note/`
        """
        json_body = {
            "note": "test1 note",
            "have_typo": False,
            "username": self.__username1,
            "sha_password": self.__sha_pass1,
        }

        response = requests.post(
            "http://0.0.0.0:8000/add-note/",
            json=json_body,
            headers=self.headers,
        )

        self.assertLess(response.status_code, 300)

        json_body = {
            "note": "test2 note",
            "have_typo": False,
            "username": self.__username2,
            "sha_password": self.__sha_pass2,
        }

        response = requests.post(
            "http://0.0.0.0:8000/add-note/",
            headers=self.headers,
            json=json_body,
        )
        self.assertLess(response.status_code, 300)

    def test_notes(self):
        """
        Testing correct works route `/notes/` for specific users
        """
        response = requests.get(
            "http://0.0.0.0:8000/notes/",
            headers=self.headers,
            params={"username": self.__username1, "sha_password": self.__sha_pass1},
        )
        json = response.json()
        self.assertIsNotNone(json["notes"])
        self.assertEqual(json["notes"]["note_0"]["username"], "test1")

        response = requests.get(
            "http://0.0.0.0:8000/notes/",
            headers=self.headers,
            params={"username": self.__username2, "sha_password": self.__sha_pass2},
        )
        json = response.json()
        self.assertIsNotNone(json["notes"])
        self.assertEqual(json["notes"]["note_0"]["username"], "test2")


if __name__ == "__main__":
    suite_other = unittest.TestLoader().loadTestsFromModule(tests)
    unittest.TextTestRunner(verbosity=2).run(suite_other)
    print()
    unittest.main(verbosity=2)
