import os

from django.http import FileResponse
from fastapi import APIRouter, Request
from fastapi.responses import ORJSONResponse, FileResponse
from fastapi_app_django_fullskack.settings import BASE_DIR

from fastapi_app_django_fullskack.settings import TEMPLATES

router = APIRouter()

@router.get("/{filepath}")
async def index(filepath: str):
    print(TEMPLATES)
    print(TEMPLATES[0]['DIRS'])
    template_root = TEMPLATES[0]['DIRS'][0]
    html_path = os.path.join(template_root , filepath)
    return FileResponse(html_path)
