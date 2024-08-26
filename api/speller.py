"""
Validation of a note for spelling errors using Yandex.Speller
"""

import asyncio
import aiohttp


async def have_errors(note_text: str) -> bool:
    """
    Check speller errors in text.
    :returns: `True` if have errors in text else `False`.
    """
    url = "https://speller.yandex.net/services/spellservice.json/checkText?text="

    async with aiohttp.ClientSession() as session:
        async with session.get(url + note_text, ssl=False) as resp:
            return bool(await resp.json())


if __name__ == "__main__":
    print(asyncio.run(have_errors(note_text="test")))
