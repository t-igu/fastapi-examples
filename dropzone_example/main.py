from fastapi import FastAPI, Request, HTTPException, status
from fastapi.responses import FileResponse, HTMLResponse
from pathlib import Path
from threading import Lock
from collections import defaultdict
import shutil
import uuid

from werkzeug.utils import secure_filename

storage_path: Path = Path(__file__).parent / "storage"
chunk_path: Path = Path(__file__).parent / "chunk"

lock = Lock()
chucks = defaultdict(list)

app=FastAPI()

@app.get("/")
def index():
    index_file = Path(__file__).parent / "index3.html"
    # print("index_file", index_file)
    if index_file.exists():
        # print("file exist", index_file)
        return HTMLResponse(index_file.read_text())

@app.post("/upload")
async def upload(request: Request):
    form = await request.form()
    file = None
    for formdata in form:
        file = form[formdata]
        # path = os.path.join("./uploads", uploadfile.filename)
        # fout = open(path, 'wb')
        # while 1:
        #     chunk = await uploadfile.read(100000)
        #     if not chunk: break
        #     fout.write (chunk)
        # fout.close()    
    if not file:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not found file")

    dz_uuid = form["dzuuid"] if "dzuuid" in form else None
    if not dz_uuid:
        # Assume this file has not been chunked
        with open(storage_path / f"{uuid.uuid4()}_{secure_filename(file.filename)}", "wb") as f:
            while 1:
                chunk = await file.read(100000)
                if not chunk: break
                f.write (chunk)
        return "File Saved"

    # Chunked download
    try:
        current_chunk = int(form["dzchunkindex"])
        total_chunks = int(form["dztotalchunkcount"])
    except KeyError as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Not all required fields supplied, missing {err}")
    except ValueError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Values provided were not in expected format")

    save_dir = chunk_path / dz_uuid

    if not save_dir.exists():
        save_dir.mkdir(exist_ok=True, parents=True)

    # Save the individual chunk
    with open(save_dir / str(form["dzchunkindex"]), "wb") as f:
        while 1:
            chunk = await file.read(100000)
            if not chunk: break
            f.write (chunk)

    # See if we have all the chunks downloaded
    with lock:
        chucks[dz_uuid].append(current_chunk)
        completed = len(chucks[dz_uuid]) == total_chunks

    # Concat all the files into the final file when all are downloaded
    if completed:
        with open(storage_path / f"{dz_uuid}_{secure_filename(file.filename)}", "wb") as f:
            for file_number in range(total_chunks):
                f.write((save_dir / str(file_number)).read_bytes())
        print(f"{file.filename} has been uploaded")
        shutil.rmtree(save_dir)

    return {"status": "OK"}

@app.get("/download/{dz_uuid}")
def download(dz_uuid):
    for file in storage_path.iterdir():
        if file.is_file() and file.name.startswith(dz_uuid):
            return FileResponse(file.resolve())
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="")
