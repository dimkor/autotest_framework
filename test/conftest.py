import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from api.BoardApi import BoardApi
from testdata.DataProvider import DataProvider
from configuration.ConfigProvider import ConfigProvider
from selenium.webdriver.firefox.options import Options

options = Options()
options.page_load_strategy = 'eager'
@pytest.fixture
def driver():
    with allure.step('Открыть и настроить браузер'):
        
        timeout = ConfigProvider().getint("ui", "timeout")
        browser_name = ConfigProvider().get("ui", "browser_name")
        
        if browser_name == 'chrome':
            driver = webdriver.Chrome()
        elif browser_name == 'ff':
            options = Options()
            options.set_preference('devtools.jsonview.enabled', False)
            driver = webdriver.Firefox(options)

        driver.maximize_window()
        driver.implicitly_wait(timeout)
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