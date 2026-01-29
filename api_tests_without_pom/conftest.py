import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 드라이버 생성 - UI 테스트용, API 테스트에서는 사용 X
@pytest.fixture(scope="session")
def driver() :
    
    options = Options()
    options.add_argument('headless')
    options.add_argument('--start-maximized')
    options.add_argument('--disable-notifications')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-gpu')
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    yield driver
    
    driver.quit()
    
@pytest.fixture
def base_url() :
    return "https://jsonplaceholder.typicode.com/"
    