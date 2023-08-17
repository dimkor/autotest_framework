import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from api.BoardApi import BoardApi
from testdata.DataProvider import DataProvider

@pytest.fixture
def driver():
    with allure.step('Открыть и настроить браузер'):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        yield driver
        
    with allure.step("Закрыть браузер"):
        driver.quit()

@pytest.fixture
def api_client() -> BoardApi:
    
    base_url = DataProvider().get('api_url')
    api_key = DataProvider().get('api_key')
    api_token = DataProvider().get('api_token')
       
    return(BoardApi(base_url, api_key, api_token))

@pytest.fixture
def test_data() -> DataProvider:
    return(DataProvider())