from fastapi import FastAPI, UploadFile, File
import tempfile

from test import check_faces

server = FastAPI(
    title="Face Verify API",
    description="Compare two face photos and check if they are the same person",
    version="1.0"
)


@server.get("/")
def home():
    return {"message": "Face Verify API is running"}


@server.post("/verify")
async def verify(
    photo1: UploadFile = File(...),
    photo2: UploadFile = File(...)
):
    # Save first uploaded photo to a temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_a:
        tmp_a.write(await photo1.read())
        path_a = tmp_a.name

    # Save second uploaded photo to a temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_b:
        tmp_b.write(await photo2.read())
        path_b = tmp_b.name

    # Run face comparison and return result
    output = check_faces(path_a, path_b)

    return output
