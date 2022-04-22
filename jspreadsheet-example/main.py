from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, ORJSONResponse

from fastapi.staticfiles import StaticFiles
from fastapi_templates import render



app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return render("index.html", {"request": request,})

@app.get("/makers")
async def index(request: Request):
    return ORJSONResponse([
        {'id':'1','name':'MAZDA'},
        {'id':'2','name':'TOYOTA'},
        {'id':'3','name':'Honda'},
    ])

@app.get("/cars")
async def index(request: Request):
    return [
        {'maker':'1','model': 'RX-7','model_year': 2001,'price': 2000},
        {'maker':'2','model': 'VOXY','model_year': 2010,'price': 5000},
        {'maker':'3','model': 'Fit','model_year': 2009,'price': 3000},
        {'maker':'3','model': 'CRV','model_year': 2010,'price': 6000},
    ]
