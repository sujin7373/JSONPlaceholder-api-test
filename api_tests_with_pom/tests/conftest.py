from utils.headers import *
from api.api_client import APIClient

@pytest.fixture
def api():
    return APIClient("https://jsonplaceholder.typicode.com")