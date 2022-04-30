from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


def get_file(filename):
    with open(filename) as f:
        s = f.read()
        return s  

@app.get("/")
async def index():
    html_text = get_file("index.html")
    return HTMLResponse(html_text)

