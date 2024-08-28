"""
API implementation
"""

from fastapi import FastAPI, status, HTTPException
from api.auth import Auth
from api.models import NoteModel
from database.engine import MongoDBEngine

# from fastapi.responses import JSONResponse

app = FastAPI()


@app.post(
    "/add-note/",
    response_description="New note added",
    status_code=status.HTTP_201_CREATED,
)
async def add_note(username="not-a-user", sha_password="not-a-pass"):
    """
    Adding new note to DB
    """

    if not Auth.validate_user(username, sha_password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Uncorrect user"
        )

    try:
        mongo_client = MongoDBEngine().create_client()

    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Server error",
        ) from exc

    return {"message": "New note added", "user": username}


@app.get("/notes/")
async def show_notes():
    """
    Showing all notes
    """
    return {"message": "showing notes"}


# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)
