import os
import sys

from loguru import logger
# import base64
# from typing import Optional
from fastapi import FastAPI, APIRouter, Depends
from fastapi.responses import ORJSONResponse
from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi_app_django_fullskack.wsgi import application as django_app
from fastapi.staticfiles import StaticFiles

from restapis.security import get_current_user
from restapis.db_utils import create_pool, terminate_pool

apps_path = os.path.join(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(apps_path)

from restapis.routers import employee, department, upload, filetransfer, code

# https://docs.djangoproject.com/ja/2.2/_modules/django/contrib/auth/

router = APIRouter()

@router.get("/v2/user/me")
def current_user(user = Depends(get_current_user)):
    return ORJSONResponse(user)

app = FastAPI(dependencies=[Depends(get_current_user)])

@app.on_event("startup")
async def startup_event():
    await create_pool()
    logger.info("app start")

@app.on_event("shutdown")
def shutdown_event():
    terminate_pool()

app.include_router(router)
app.include_router(department.router, prefix="/v2/department", tags=["department"],)
app.include_router(employee.router, prefix="/v2/employee", tags=["employee"],)
app.include_router(upload.router, prefix="/v2/upload", tags=["upload"],)
app.include_router(filetransfer.router, prefix="/v2/filetransfer", tags=["filetransfer"],)
app.include_router(code.router, prefix="/v2/code", tags=["code"],)

app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("", WSGIMiddleware(django_app))
