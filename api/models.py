"""
Models to request and response 
"""

from pydantic import BaseModel, PositiveInt

class NoteModel(BaseModel):
    """
    Note structure
    """

    _id: PositiveInt
    username: str
    note_text: str
    have_speller: bool
