import pytest
import allure
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from pages.LoginPage import LoginPage
# from testdata.DataProvider import DataProvider

class MainPage:
    
    # url = 'https://trello.com/u/nitib72125/boards'
    url = 'https://trello.com'
    
    # data = DataProvider()
    # token = data.get('token')
    
    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver
        # self.__driver.get(self.url)
        # self.__driver.add_cookie({'token': self.token})
        self.__driver.get(self.url)


    def create_board(self):
        self.__driver.find_element(By.CSS_SELECTOR, 'div[class="board-tile mod-add"]').click()

        self.__driver.find_element(By.CSS_SELECTOR, 'input[data-testid="create-board-title-input"]').clear()
        
        self.__driver.find_element(By.CSS_SELECTOR, 'input[data-testid="create-board-title-input"]').send_keys('test board')
        
        WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable, (By.CSS_SELECTOR, 'button[data-testid="create-board-submit-button"]'))
        
        self.__driver.find_element(By.CSS_SELECTOR, 'button[data-testid="create-board-submit-button"]').click()
        sleep(5)
        