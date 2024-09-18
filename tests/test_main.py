import pytest

from src import hotmix as hm


def test_hello_world_works(client1):
    res = client1.get("/hello_world")
    assert res.text == "<div>Hello world</div>"


def test_using_nonexisting_template_raises_exception(client1):
    with pytest.raises(hm.TemplateNotFoundError) as excinfo:
        res = client1.get("/nonexisting_template")
    assert str(excinfo.value) == "nonexisting_template.html"


def test_template_contains_api_result_parameter(client1):
    res = client1.get("/template_with_api_result_parameter")
    assert res.text == "<div>Parameter: 5</div>"


def test_template_contains_request_parameter(client1):
    res = client1.get("/template_with_request_parameter")
    assert res.text == "<div>Path: /template_with_request_parameter</div>"
