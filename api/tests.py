"""
Tests for client service
"""

import unittest
from unittest import IsolatedAsyncioTestCase
from .auth import Auth
from .speller import have_errors

class TestAuthMethods(unittest.TestCase):
    """
    Testing Auth module
    """

    def test_auth_user_test1(self):
        """
        Testing auth test1 user
        """
        self.assertEqual(Auth.authentication_user("test1", "test1"), True)
        self.assertEqual(Auth.authentication_user("test1", "test"), False)
        self.assertFalse(Auth.authentication_user("test", "test1"))

    def test_auth_user_test2(self):
        """
        Testing auth test2 user
        """
        self.assertTrue(Auth.authentication_user("test1", "test1"))
        self.assertEqual(Auth.authentication_user("test2", "test1"), False)
        test_pass = "60303ae22b998861bce3b28f33eec1be758a213c86c93c076dbe9f558c11c752"
        self.assertFalse(Auth.authentication_user("test2", test_pass))

    def test_validate_users(self):
        """
        Testing validation users
        """
        test_pass = "60303ae22b998861bce3b28f33eec1be758a213c86c93c076dbe9f558c11c752"
        self.assertTrue(Auth.validate_user("test2", test_pass))
        self.assertFalse(Auth.validate_user("test2", "test2"))


class TestSpellerFunc(IsolatedAsyncioTestCase):
    """
    Async siute for testing
    """

    async def test_speller(self):
        """
        Testing speller func
        """
        self.assertFalse(await have_errors("False"))
        self.assertFalse(await have_errors("True"))
        self.assertFalse(await have_errors("some text"))
        self.assertTrue(await have_errors("some text with errror"))
        self.assertTrue(await have_errors("some text with errrors"))

        self.assertFalse(await have_errors("Немного по-русски"))
        self.assertTrue(await have_errors("Немного непо-русски"))


if __name__ == "__main__":
    unittest.main()
