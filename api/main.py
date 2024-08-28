"""
API implementation
"""

from fastapi import FastAPI, status, HTTPException, Response, Request
from pydantic import BaseModel
from api.auth import Auth
from api.models import NoteModel
from api.speller import have_errors
from database.engine import MongoDBEngine

from fastapi.responses import JSONResponse


class RequestModel(BaseModel):
    note: str
    have_speller: bool = False
    usename: str
    sha_password: str


app = FastAPI()


@app.post(
    "/add-note/",
    status_code=status.HTTP_201_CREATED,
)
async def add_note(body: RequestModel):
    """
    Adding new note to DB
    """
    if not Auth.validate_user(body.usename, body.sha_password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Uncorrect user"
        )

    # Await the coroutine to get the boolean result
    speller = await have_errors(body.note)

    note = NoteModel(username=body.usename, note_text=body.note, have_speller=speller)

    try:
        mongo = MongoDBEngine()
        db_client = mongo.create_client()
        db = db_client[mongo.get_db_name()]
        db.notes.insert_one(note.model_dump())

    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Server error",
        ) from exc

    user = body.usename

    return {"message": f"New note added for {user}"}


@app.get("/notes/")
async def show_notes(username, sha_password):
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
        content={"message": "showing notes", "notes": content},
        media_type="application/json",
    )

    return response


# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)
