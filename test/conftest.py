import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from api.BoardApi import BoardApi


@pytest.fixture
def driver():
    with allure.step('Открыть и настроить браузер'):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(4)
        yield driver
        
    with allure.step("Закрыть браузер"):
        driver.quit()

@pytest.fixture
def api_client() -> BoardApi:
    
    base_url = 'https://api.trello.com/1'
    api_key = '9a4c098cfc8b126b70975af522e016cf'
    api_token = 'ATTA84feb27d467f7cefcc9ac45012deec4c4fc476e62b6f578c3393cfc5a881a508A8B85F15'
       
    return(BoardApi(base_url, api_key, api_token))