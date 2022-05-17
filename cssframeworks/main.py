import os
import sys

from sqlalchemy import true
import uvicorn
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


@app.get("/uikit/template", response_class=HTMLResponse)
async def flexbox(request: Request):
    return templates.TemplateResponse("uikit/uikit-template.html", {"request": request,})

@app.get("/uikit/components", response_class=HTMLResponse)
async def flexbox(request: Request):
    return templates.TemplateResponse("uikit/components.html", {"request": request,})

@app.get("/uikit/upload", response_class=HTMLResponse)
async def flexbox(request: Request):
    return templates.TemplateResponse("uikit/upload.html", {"request": request,})

@app.get("/bulma/template", response_class=HTMLResponse)
async def flexbox(request: Request):
    return templates.TemplateResponse("bulma/bulma-template.html", {"request": request,})

@app.get("/bulma/components", response_class=HTMLResponse)
async def flexbox(request: Request):
    return templates.TemplateResponse("bulma/components.html", {"request": request,})

@app.get("/bulma/upload", response_class=HTMLResponse)
async def flexbox(request: Request):
    return templates.TemplateResponse("bulma/upload.html", {"request": request,})

@app.get("/bootstrap/template", response_class=HTMLResponse)
async def flexbox(request: Request):
    return templates.TemplateResponse("bootstrap/bootstrap-template.html", {"request": request,})

@app.get("/bootstrap/components", response_class=HTMLResponse)
async def flexbox(request: Request):
    return templates.TemplateResponse("bootstrap/components.html", {"request": request,})

@app.get("/bootstrap/upload", response_class=HTMLResponse)
async def flexbox(request: Request):
    return templates.TemplateResponse("bootstrap/upload.html", {"request": request,})

@app.get("/noclass/tacit", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("noclass/tacit.html", {"request": request,})

@app.get("/noclass/simple", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("noclass/simple.html", {"request": request,})

@app.get("/noclass/mvp", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("noclass/mvp.html", {"request": request,})

@app.get("/noclass/mini", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("noclass/mini.html", {"request": request,})

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