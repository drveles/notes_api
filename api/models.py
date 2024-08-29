"""
Models to request and response 
"""

from pydantic import BaseModel, PositiveInt

class NoteModel(BaseModel):
    """
    Note structure in MongoDB
    """
    _id: PositiveInt
    username: str
    note_text: str
    have_typo: bool
