import os
from fastapi import APIRouter, Request, HTTPException, status
from fastapi.responses import FileResponse, HTMLResponse, ORJSONResponse
from pathlib import Path
from threading import Lock
from collections import defaultdict
import shutil
import uuid
from django.conf import settings

storage_path: Path = settings.BASE_DIR / "uploads" / "files"
chunk_path: Path = settings.BASE_DIR / "uploads" / "temp"

lock = Lock()
chucks = defaultdict(list)

router=APIRouter()

def get_save_path(dirname: str, filename: str):

    save_path = storage_path.parent / dirname / filename

    return save_path

@router.post("/upload")
async def upload(request: Request):
    
    form = await request.form()
    file = None
    for formdata in form:
        file = form[formdata]

    if not file:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not found file")

    dz_uuid = form["dzuuid"] if "dzuuid" in form else None

    save_dir = form["save_dir"]

    save_path = get_save_path(save_dir[1:], file.filename)

    # print("save_path", save_path)

    if not dz_uuid:
        # Assume this file has not been 
        with open(save_path, "wb") as f:
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

    # chunked save directory
    chunk_save_dir = chunk_path / dz_uuid

    if not chunk_save_dir.exists():
        chunk_save_dir.mkdir(exist_ok=True, parents=True)

    # Save the individual chunk
    with open(chunk_save_dir / str(form["dzchunkindex"]), "wb") as f:
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
        with open(save_path, "wb") as f:
            for file_number in range(total_chunks):
                f.write((chunk_save_dir / str(file_number)).read_bytes())
        print(f"{file.filename} has been uploaded")
        shutil.rmtree(chunk_save_dir)

    return "Chunk upload successful"

@router.get("/download")
def download(filename:str):
    for file in storage_path.iterdir():
        if file.is_file() and file.name == filename:
            return FileResponse(file.resolve())
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="")

@router.get("/structure")
def get_directories(directory: str):

    dirs = {}
    real_path = os.path.join(str(storage_path.parent) , directory[1:])

    # print("real_path", storage_path.parent,  real_path)
    for current_dir, sub_dirs, files_list in os.walk(real_path):
        dirname = current_dir.replace(str(storage_path.parent), "")
        children = [{"name": sub_dir, "type":"d"} for sub_dir in sub_dirs]
        children.extend([{"name": file, "type":"f"} for file in files_list])
        dirs[dirname] = {
                "name": os.path.basename(current_dir),
                "children": children,
            }
    # print("dirs", dirs)
    return ORJSONResponse(dirs)
