from functools import wraps
from fastapi import Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
import os


from .exceptions import *


templates = None
templates_path: str = ""


def init(_templates_path):
    global templates, templates_path

    templates_path = _templates_path
    templates = Jinja2Templates(directory=templates_path)


def template_exists(file_name):
    path = os.path.join(templates_path, file_name)
    return os.path.exists(path)


def htmx(template_name):
    def htmx_decorator(func):

        @wraps(func)
        async def wrapper(request: Request, *args, **kwargs):
            data = await func(request, *args, **kwargs)
            if data == None:
                data = {}

            file_name = f"{template_name}.html"

            if not template_exists(file_name):
                raise TemplateNotFoundError(file_name)

            context = {"request": request}
            context.update(data)
            return templates.TemplateResponse(file_name, context)

        return wrapper

    return htmx_decorator
