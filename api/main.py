"""
API implementation
"""

from fastapi import FastAPI, status, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from notes_api.database.engine import MongoDBEngine
from .auth import Auth
from .models import NoteModel
from .speller import have_errors


class RequestModel(BaseModel):
    """
    Model for HTTP request body
    """

    note: str
    have_typo: bool = False
    username: str
    sha_password: str


app = FastAPI()


@app.post(
    "/add-note/",
    status_code=status.HTTP_201_CREATED,
)
async def add_note(body: RequestModel) -> JSONResponse:
    """
    Adding new note to DB
    """
    if not Auth.validate_user(body.username, body.sha_password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Uncorrect user",
            headers={"Content-Type": "application/json"},
        )

    speller = await have_errors(body.note)
    note = NoteModel(username=body.username, note_text=body.note, have_typo=speller)

    try:
        mongo = MongoDBEngine()
        db_client = mongo.create_client()
        db = db_client[mongo.get_db_name()]
        db.notes.insert_one(note.model_dump())

    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Server error",
            headers={"Content-Type": "application/json"},
        ) from exc

    user = body.username

    response = JSONResponse(
        content={"detail": f"New note added for {user}"},
        media_type="application/json",
        headers={"Content-Type": "application/json"},
    )

    return response


@app.get("/notes/")
async def show_notes(username: str, sha_password: str) -> JSONResponse:
    """
    Showing all notes
    """
    if not Auth.validate_user(username, sha_password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Uncorrect user",
        )

    mongo = MongoDBEngine()
    db_client = mongo.create_client()
    db = db_client[mongo.get_db_name()]
    collection = db[mongo.get_db_collection()]
    content = {}

    for idx, document in enumerate(collection.find({"username": username})):
        document["_id"] = str(document["_id"])
        content[f"note_{idx}"] = document

    response = JSONResponse(
        content={"detail": "showing notes", "notes": content},
        media_type="application/json",
        headers={"Content-Type": "application/json"},
    )

    return response
