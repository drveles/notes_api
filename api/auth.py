"""
Created users to acces notes
"""

import hashlib


class Auth:
    """
    Name of user and his password in sha256
    """

    __users_sha_passwords = {
        "admin": "8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918",
        "test1": "1b4f0e9851971998e732078544c96b36c3d01cedf7caa332359d6f1d83567014",
        "test2": "60303ae22b998861bce3b28f33eec1be758a213c86c93c076dbe9f558c11c752",
        "user1": "0a041b9462caa4a31bac3567e0b6e6fd9100787db2ab433d96f6d178cabfce90",
        "user2": "6025d18fe48abd45168528f18a82e265dd98d421a7084aa09f61b341703901a3",
    }

    @classmethod
    def authentication_user(cls, username: str, password: str) -> bool:
        """
        Checking user password to co
        """
        curr_sha_password = hashlib.sha256(password.encode("ascii")).hexdigest()
        stock_sha_password = cls.__users_sha_passwords.get(username, "")

        return curr_sha_password == stock_sha_password

    @classmethod
    def validate_user(cls, username: str, sha_password: str) -> bool:
        """
        Checking user password to co
        """
        stock_sha_password = cls.__users_sha_passwords.get(username, "")

        return sha_password == stock_sha_password
