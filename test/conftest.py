import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    with allure.step('Открыть и настроить браузер'):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(4)
        yield driver
        
    with allure.step("Закрыть браузер"):
        driver.quit()
