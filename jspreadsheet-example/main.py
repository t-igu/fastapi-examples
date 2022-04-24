from pydantic import BaseModel

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, ORJSONResponse


from fastapi.staticfiles import StaticFiles
from fastapi_templates import render

# リクエストbodyを定義
class Car(BaseModel):
    id: int
    maker: str
    model: str
    model_year: str
    price: int

app = FastAPI()



app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/simple", response_class=HTMLResponse)
async def index(request: Request):
    return render("simple.html", {"request": request,})

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
        {'id':1,'maker':'1','model': 'RX-7','model_year': 2001,'price': 2000},
        {'id':2,'maker':'2','model': 'VOXY','model_year': 2010,'price': 5000},
        {'id':3,'maker':'3','model': 'Fit','model_year': 2009,'price': 3000},
        {'id':4,'maker':'3','model': 'CRV','model_year': 2010,'price': 6000},
    ]

@app.get("/cars/create")
async def cars_create(request: Request):
    return {'id':None,'maker': None,'model': None,'model_year': None,'price': None}

@app.post("/cars/create")
async def cars_create(request: Request, car: Car):
    return {"status": "OK"}

@app.post("/cars/update/{id}")
async def cars_upadte(request: Request, id: int, car: Car):
    return {"status": "OK"}

@app.post("/cars/detete/{id}")
async def cars_delete(request: Request, id: int, car: Car):
    return {"status": "OK"}
