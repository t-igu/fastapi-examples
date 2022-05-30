import os
import sys

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

apps_path = os.path.join(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(apps_path)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.on_event("startup")
async def startup_event():
    pass

@app.on_event("shutdown")
async def shutdown_event():
    pass

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request,})

@app.get("/{framework}/{filename}", response_class=HTMLResponse)
async def flexbox(request: Request, framework:str, filename: str):
    return templates.TemplateResponse(f"{framework}/{filename}.html", {"request": request,})

@app.post("/fileupload")
async def fileupload_post(request: Request):
    '''docstring
    アップロードされたファイルを保存する
    '''
    form = await request.form()
    # uploadedpath = "./uploads"
    # files = os.listdir(uploadedpath)
    for formdata in form:
        uploadfile = form[formdata]
        print(uploadfile.filename)
        # path = os.path.join("./uploads", uploadfile.filename)
        # fout = open(path, 'wb')
        # while 1:
        #     chunk = await uploadfile.read(100000)
        #     if not chunk: break
        #     fout.write (chunk)
        # fout.close()
    return {"status":"OK"}
