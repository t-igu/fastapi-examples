import os

from django.http import FileResponse
from fastapi import APIRouter, Request
from fastapi.responses import ORJSONResponse, FileResponse
from fastapi_app_django_fullskack.settings import BASE_DIR

import starlette

router = APIRouter()

uploadedpath = os.path.join(BASE_DIR, "uploads")

def get_extention(filePath):
    '''docstring
    ファイルパスから拡張子を取得する
    '''
    ex = os.path.splitext(filePath)
    return ex[len(ex)-1]

@router.get("/")
async def index():
    filenmes = os.listdir(uploadedpath)
    filelist = [{
        "filename":f, 
        "filesize": os.path.getsize(os.path.join(uploadedpath, f)),    
        "extention": get_extention(f),
    } for f in filenmes if os.path.isfile(os.path.join(uploadedpath, f))]
    return ORJSONResponse(filelist)

@router.post("/upload")
async def fileupload_post(request: Request):
    '''docstring
    アップロードされたファイルを保存する
    '''
    form = await request.form()
    for formdata in form:
        # print(formdata)
        uploadfile = form[formdata]
        if isinstance(uploadfile, starlette.datastructures.UploadFile):
            path = os.path.join(uploadedpath, uploadfile.filename)
            fout = open(path, 'wb')
            while 1:
                chunk = await uploadfile.read(100000)
                if not chunk: break
                fout.write (chunk)
            fout.close()

    return await index()

@router.get("/download/{filename}")
async def file_delete(filename:str):
    '''docstring
    ファイルをダウンロードする
    '''
    filepath = os.path.join(uploadedpath, filename)
    return FileResponse(filepath)

@router.post("/delete/{filename}")
async def file_delete(filename:str):
    '''docstring
    ファイルを削除する
    '''
    filepath=os.path.join(uploadedpath, filename)
    os.remove(filepath)
    return await index()
