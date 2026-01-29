from utils.headers import *

class APIClient :
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        
    def get(self, endpoint) :
        url = f"{self.base_url}{endpoint}"
        return self.session.get(url)
    
    def post(self, endpoint, payload=None) :
        url = f"{self.base_url}{endpoint}"
        return self.session.post(url, json=payload)
    
    def put(self, endpoint, payload=None) :
        url = f"{self.base_url}{endpoint}"
        return self.session.put(url, json=payload)
    
    def delete(self, endpoint) :
        url = f"{self.base_url}{endpoint}"
        return self.session.delete(url)