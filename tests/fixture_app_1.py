from fastapi import FastAPI, Request
from src import hotmix as hm


app = FastAPI()
hm.init("tests/templates")


@app.get("/hello_world")
@hm.htmx("hello_world")
async def index(request: Request):
    pass


@app.get("/nonexisting_template")
@hm.htmx("nonexisting_template")
async def index(request: Request):
    pass


@app.get("/template_with_api_result_parameter")
@hm.htmx("template_with_api_result_parameter")
async def index(request: Request):
    return {"param": 5}


@app.get("/template_with_request_parameter")
@hm.htmx("template_with_request_parameter")
async def index(request: Request):
    pass
