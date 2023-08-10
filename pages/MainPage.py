import pytest
import allure
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from pages.LoginPage import LoginPage


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

    @allure.step('Создание доски')   
    def create_board(self):
        self.__driver.find_element(By.CSS_SELECTOR, 'div[class="board-tile mod-add"]').click()

        self.__driver.find_element(By.CSS_SELECTOR, 'input[data-testid="create-board-title-input"]').clear()
        self.__driver.find_element(By.CSS_SELECTOR, 'input[data-testid="create-board-title-input"]').send_keys('test board')
        
        create_button = self.__driver.find_element(By.CSS_SELECTOR, 'button[data-testid="create-board-submit-button"]')
        while create_button.is_enabled() == False:
            WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable, (By.CSS_SELECTOR, 'button[data-testid="create-board-submit-button"]'))
        
        self.__driver.find_element(By.CSS_SELECTOR, 'button[data-testid="create-board-submit-button"]').click()
        sleep(5)
    
    @allure.step('Удаление доски')   
    def delete_board(self) -> None:
        
        with allure.step('Клик на доску "___"'):
            WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable, (By.CSS_SELECTOR, 'div[title="test board"]'))
            self.__driver.find_element(By.CSS_SELECTOR, 'div[title="test board"]').click()
        
        WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable, (By.CSS_SELECTOR, 'h1[data-testid="board-name-display"]'))
        
        with allure.step('Клик на три точки'):
            WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable, (By.CSS_SELECTOR, 'button[aria-label="Меню"]'))
            self.__driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Меню"]').click()
        
        with allure.step('Клик на "Ещё"'):
            WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable, (By.CSS_SELECTOR, 'a[class="board-menu-navigation-item-link js-open-more"]'))
            self.__driver.find_element(By.CSS_SELECTOR, 'a[class="board-menu-navigation-item-link js-open-more"]').click()
            sleep(3)
            # self.__driver.find_element(By.CSS_SELECTOR, 'a[class="board-menu-navigation-item-link js-open-more"]').click()
        
        with allure.step('Клик на "Закрыть доску"'):
            WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable, (By.CSS_SELECTOR, 'a[class="board-menu-navigation-item-link js-close-board"]'))
            self.__driver.find_element(By.CSS_SELECTOR, 'a[class="board-menu-navigation-item-link js-close-board"]').click()
        
        with allure.step('Клик на "Закрыть"'):
            WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable, (By.CSS_SELECTOR, 'input[class^="js-confirm"]'))
            self.__driver.find_element(By.CSS_SELECTOR, 'input[class^="js-confirm"]').click()
        
        with allure.step('Клик на "удалить доску навсегда"'):
            WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable, (By.CSS_SELECTOR, 'button[data-testid="close-board-delete-board-button"]'))
            self.__driver.find_element(By.CSS_SELECTOR, 'button[data-testid="close-board-delete-board-button"]').click()
        
        with allure.step('клик на "Удалить" в модальном окне'):
            WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable, (By.CSS_SELECTOR, 'button[data-testid="close-board-delete-board-confirm-button"]'))
            self.__driver.find_element(By.CSS_SELECTOR, 'button[data-testid="close-board-delete-board-confirm-button"]').click()
        
        WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable, (By.CSS_SELECTOR, 'span[data-testid="home-team-tab-name"]'))
        sleep(10)

    @allure.step('Создание карточки')    
    def create_card(self) -> None:
        
        self.__driver.find_element(By.CSS_SELECTOR, 'div[class="board-tile mod-add"]').click()

        self.__driver.find_element(By.CSS_SELECTOR, 'input[data-testid="create-board-title-input"]').clear()
        self.__driver.find_element(By.CSS_SELECTOR, 'input[data-testid="create-board-title-input"]').send_keys('test board')
        
        create_button = self.__driver.find_element(By.CSS_SELECTOR, 'button[data-testid="create-board-submit-button"]')
        while create_button.is_enabled() == False:
            WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located, (By.CSS_SELECTOR, 'button[data-testid="create-board-submit-button"]'))
        
        self.__driver.find_element(By.CSS_SELECTOR, 'button[data-testid="create-board-submit-button"]').click()
        
        with allure.step('Клик по "Добавить список"'):
            WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located, (By.CSS_SELECTOR, 'div[class="js-add-list list-wrapper mod-add is-idle"]'))
            self.__driver.find_element(By.CSS_SELECTOR, 'div[class="js-add-list list-wrapper mod-add is-idle"]').click()
        
        # ввести загол списка
        with allure.step('Заполнение названия карточки'):
            WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located, (By.CSS_SELECTOR, 'input[class="list-name-input"]'))
            self.__driver.find_element(By.CSS_SELECTOR, 'input[class="list-name-input"]').clear()
            self.__driver.find_element(By.CSS_SELECTOR, 'input[class="list-name-input"]').send_keys('Список 1')
        
        with allure.step('Клик по кнопке "Добавить карточку"'):
            WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located, (By.CSS_SELECTOR, 'span[class="js-add-a-card"]'))
            self.__driver.find_element(By.CSS_SELECTOR, 'span[class="js-add-a-card"]').click()
        
        with allure.step('Ввести заголовок для этой карточки'):
            WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located, (By.CSS_SELECTOR, 'textarea[class="list-card-composer-textarea js-card-title"]'))
            self.__driver.find_element(By.CSS_SELECTOR, 'textarea[class="list-card-composer-textarea js-card-title"]').clear()
            self.__driver.find_element(By.CSS_SELECTOR, 'textarea[class="list-card-composer-textarea js-card-title"]').send_keys('Карточка 1')
        
        with allure.step('Клик по "Добавить карточку"'):
            WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located, (By.CSS_SELECTOR, 'input[class="nch-button nch-button--primary confirm mod-compact js-add-card"]'))
            self.__driver.find_element(By.CSS_SELECTOR, 'input[class="nch-button nch-button--primary confirm mod-compact js-add-card"]').click()
        
        with allure.step('Клик по борду'):
            WebDriverWait(self.__driver, 10).until(EC.presence_of_element_locateds, (By.CSS_SELECTOR, '#board"]'))
            self.__driver.find_element(By.CSS_SELECTOR, '#board"]').click()