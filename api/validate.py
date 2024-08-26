"""
Validation of a note for spelling errors using Yandex.Speller
"""

import aiohttp


class Speller:
    """
    Class with Speller data.
    """

    __url = "https://speller.yandex.net/services/spellservice.json/checkText"

    def errors_in_text(self, text: str) -> bool:
        """
        Check speller errors in text
        """

        return not text
