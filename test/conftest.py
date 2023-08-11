import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    with allure.step('Открыть и настроить браузер'):
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(15)
        yield driver
        
    with allure.step("Закрыть браузер"):
        driver.quit()
