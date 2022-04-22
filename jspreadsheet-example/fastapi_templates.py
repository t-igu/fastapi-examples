from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

def render(filename, kwargs):
    return templates.TemplateResponse(filename, kwargs)