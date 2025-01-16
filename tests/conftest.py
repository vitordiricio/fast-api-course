import pytest
from fastapi.testclient import TestClient

from fast_api_course.app import app


@pytest.fixture
def client():
    return TestClient(app)
