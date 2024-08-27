"""
API implementation
"""

from fastapi import FastAPI, status

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

    return {"message": "note added", "user": username, "pass": sha_password}


@app.get(
    "/notes/",
)
async def show_notes():
    """
    Showing all notes
    """
    return {"message": "showing notes"}
