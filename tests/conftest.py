import pytest
from fastapi.testclient import TestClient


from .fixture_app_1 import app as app1


@pytest.fixture
def client1():
    yield TestClient(app1)
