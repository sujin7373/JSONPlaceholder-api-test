from utils.headers import *
from api.api_client import APIClient

@pytest.fixture
def api():
    return APIClient("https://jsonplaceholder.typicode.com")

@pytest.fixture
def create_payload() :
    return {
        "title": "classic",
        "body": "fly me to the moon",
        "userId": 1
    }
    
@pytest.fixture
def update_payload() :
    return {
        "title": "classic_updated",
        "body": "Lovely Girl"
    }
    
@pytest.fixture
def common_headers() :
    return {
        "Content-Type" : "application/json; charset=UTF-8"
    }