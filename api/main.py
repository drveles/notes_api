"""
API implementation
"""

from fastapi import FastAPI, status

# from fastapi.responses import JSONResponse

app = FastAPI()


@app.post("/add-note/")
async def add_note(username="not-a-user", sha_password="not-a-pass"):
    """
    Adding new note to DB
    """

    return {"message": "adding note", "user": username, "pass": sha_password}


@app.get("/notes/", status_code=status.HTTP_201_CREATED)
async def show_notes():
    """
    Showing all notes
    """
    return {"message": "showing notes"}
