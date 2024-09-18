# About

HotMix allows you to conveniently add htmx to your FastAPI app.





# Getting Started

Install the packages

```
pip install hotmix, fastapi, uvicorn
```



Create a tempate folder and add a template.

```
main.py
templates/
	index.html
```



Content of `index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Page</title>
</head>
<body>
    <h1>HotMix Hello World</h1>
    <p>Parameter from the API: {{ param }}</p>
    <p>You are accessing the path: {{ request.url.path }}</p>
</body>
</html>
```



Content of `main.py`

```python
from fastpai import FastAPI, Request
import hotmix as hm

app = FastAPI()
hm.init("templates")

@app.get("/")
@hm.htmx("index")
def main(request: Request):
    return {"param": 37}
```



# How it works

Initialize hotmix while setting the templates folder path

```python
import hotmix as hm

hm.init("templates")
```



For each of the routes which should return some htmx content, add a decorator specifying the name of the template file, without the `.html` extension.

```python
@app.get("/")
@hm.htmx("index")
def main(request: Request):
    return {"param": 37}
```

Instead of returning the dictionary as JSON data, it will pass the dictionary to the jinja2 template engine, which will return the `.html` with the desired parameters.

HotMix can handle two kinds of parameters:

- Explicit paramters: returned in the request answer dictionary. They are accessed by giving their names: `{{ param }}`.
- Request parameters, accessed through the `request` keyword. For example `{{ request.url.path }}`.

