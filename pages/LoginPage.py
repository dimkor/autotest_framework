import pytest
import allure
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from testdata.DataProvider import DataProvider

class LoginPage:
    
    base_url = DataProvider().get('url')
    
    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver
        self.__driver.get(self.base_url + 'login')
    
    @allure.step('Авторизация с парой {email}:{password}')   
    def auth(self, email: str, password: str) -> None:
        """
        Авторизация

        Args:
            email (str): email
            password (str): пароль
        """
        with allure.step('Заполнение поля email'):
            self.__driver.find_element(By.CSS_SELECTOR, 'input[id="user"]').clear()
            self.__driver.find_element(By.CSS_SELECTOR, 'input[id="user"]').send_keys(email)
        
        with allure.step('Нажатие кнопки "Продолжить"'):
            self.__driver.find_element(By.CSS_SELECTOR, 'input[id="login"]').click()

        #ожидание отрисовки поля Пароль
        WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "svg[role=presentation]")))
        
        with allure.step('Заполнение поля password'):
            self.__driver.find_element(By.CSS_SELECTOR, 'input[id="password"]').clear()
            self.__driver.find_element(By.CSS_SELECTOR, 'input[id="password"]').send_keys(password)
        
        with allure.step('Нажатие кнопки "Войти"'):
            self.__driver.find_element(By.CSS_SELECTOR, 'button[id="login-submit"]').click()

        WebDriverWait(self.__driver, 15).until(EC.visibility_of_element_located, (By.CSS_SELECTOR, '.boards-page-section-header-name'))

    @allure.step('Клик по юзерпику')     
    def open_menu(self) -> None:
        locator = 'button[data-testid="header-member-menu-button"]>div>span'
        WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located, locator)
        self.__driver.find_element(By.CSS_SELECTOR, locator).click()
        
    def return_user_email(self) -> str:
        locator = 'div[data-testid="account-menu-account-section"]>div>div:last-child>div:last-child'
        return self.__driver.find_element(By.CSS_SELECTOR, locator).text