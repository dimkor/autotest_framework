import pytest
import allure
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver import ActionChains
import json

from pages.LoginPage import LoginPage
import urllib.parse

class MainPage:
    
    url = 'https://trello.com'
    
    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver
        self.__driver.get(self.url+'/u/automation_user/boards')
        
        with allure.step('Устанавливаем куки авторизации'):
            cookie = {
                "name":"token",
                "value": '64cf25acc9f789ff5ee14224/ATTSwXK8BbrO0tNOqw1gVyHkCVM0GcKzliLbTLXWKlfaQsZ26KkVbdKCelhuQqWESn8q282037AB'
            }
            self.__driver.add_cookie(cookie)
        
        my_try = 0    
        while self.__driver.title.startswith('Ошибка'):
            with allure.step('Открываем рабочее пространство пользователя'):
                self.__driver.get(self.url+'/u/automation_user/boards')
            #выход из цикла в том случае, если 10 раз нас постигает неудача
            my_try = +1
            if my_try == 9:
                break

    @allure.step('Создание доски')   
    def create_board(self, boardname: str) -> str:

        self.__driver.find_element(By.CSS_SELECTOR, 'div[class="board-tile mod-add"]').click()

        self.__driver.find_element(By.CSS_SELECTOR, 'input[data-testid="create-board-title-input"]').clear()
        self.__driver.find_element(By.CSS_SELECTOR, 'input[data-testid="create-board-title-input"]').send_keys(boardname)
        
        create_button = self.__driver.find_element(By.CSS_SELECTOR, 'button[data-testid="create-board-submit-button"]')
        while create_button.is_enabled() == False:
            WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable, (By.CSS_SELECTOR, 'button[data-testid="create-board-submit-button"]'))
        
        self.__driver.find_element(By.CSS_SELECTOR, 'button[data-testid="create-board-submit-button"]').click()

        boardname = urllib.parse.quote(boardname.lower().replace(' ', '-'))

        current_url = self.__driver.current_url

        while current_url.endswith(boardname) == False:
            WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located, (By.CSS_SELECTOR, 'div[data-testid="board-share-button"]'))
            current_url = self.__driver.current_url

    @allure.step('Удаление доски')   
    def delete_board(self, boardname: str) -> None:
    
        with allure.step('Клик на доску "___"'):
            WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable, (By.CSS_SELECTOR, f'div[title="{boardname}"]'))
            self.__driver.find_element(By.CSS_SELECTOR, f'div[title="{boardname}"]').click()
        
        WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable, (By.CSS_SELECTOR, 'h1[data-testid="board-name-display"]'))
        
        with allure.step('Клик на три точки'):
            WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable, (By.CSS_SELECTOR, 'button[aria-label="Меню"]'))
            self.__driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Меню"]').click()
        
        with allure.step('Клик на "Ещё"'):
            WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable, (By.CSS_SELECTOR, 'a[class="board-menu-navigation-item-link js-open-more"]'))
            self.__driver.find_element(By.CSS_SELECTOR, 'a[class="board-menu-navigation-item-link js-open-more"]').click()
            # self.__driver.find_element(By.CSS_SELECTOR, 'a[class="board-menu-navigation-item-link js-open-more"]').click()
        
        with allure.step('Клик на "Закрыть доску"'):
            WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable, (By.CSS_SELECTOR, 'a[class="board-menu-navigation-item-link js-close-board"]'))
            self.__driver.find_element(By.CSS_SELECTOR, 'a[class="board-menu-navigation-item-link js-close-board"]').click()
        
        with allure.step('Клик на "Закрыть"'):
            WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable, (By.CSS_SELECTOR, 'input[class^="js-confirm"]'))
            self.__driver.find_element(By.CSS_SELECTOR, 'input[class^="js-confirm"]').click()
        
        with allure.step('Клик на "Удалить доску навсегда"'):
            WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable, (By.CSS_SELECTOR, 'button[data-testid="close-board-delete-board-button"]'))
            self.__driver.find_element(By.CSS_SELECTOR, 'button[data-testid="close-board-delete-board-button"]').click()
        
        with allure.step('Клик на "Удалить" в модальном окне'):
            WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable, (By.CSS_SELECTOR, 'button[data-testid="close-board-delete-board-confirm-button"]'))
            self.__driver.find_element(By.CSS_SELECTOR, 'button[data-testid="close-board-delete-board-confirm-button"]').click()
        
        self.__driver.get(self.url)

    @allure.step('Создание карточки')    
    def create_card(self, boardname: str, card_name: str) -> None:
        
        self.create_board(boardname)
        
        with allure.step('Клик по "Добавить список"'):
            WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located, (By.CSS_SELECTOR, 'div[id="board"]>div:last-child'))
            self.__driver.find_element(By.CSS_SELECTOR, 'div[id="board"]>div:last-child').click()
        
        with allure.step('Заполнение названия карточки'):
            WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located, (By.CSS_SELECTOR, 'input[class="list-name-input"]'))
            self.__driver.find_element(By.CSS_SELECTOR, 'input[class="list-name-input"]').clear()
            self.__driver.find_element(By.CSS_SELECTOR, 'input[class="list-name-input"]').send_keys('Список 1')
        
        with allure.step('Клик по кнопке "Добавить список"'):
            WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located, (By.CSS_SELECTOR, 'input[value="Добавить список"]'))
            self.__driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()
        
        with allure.step('Клик по "Добавить карточку"'):
            WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located, (By.CSS_SELECTOR, 'a[class="open-card-composer js-open-card-composer"]'))
            self.__driver.find_element(By.CSS_SELECTOR, 'a[class="open-card-composer js-open-card-composer"]').click()

        with allure.step('Ввести заголовок для этой карточки'):
            WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located, (By.CSS_SELECTOR, 'textarea[class="list-card-composer-textarea js-card-title"]'))
            self.__driver.find_element(By.CSS_SELECTOR, 'textarea[class="list-card-composer-textarea js-card-title"]').clear()
            self.__driver.find_element(By.CSS_SELECTOR, 'textarea[class="list-card-composer-textarea js-card-title"]').send_keys(card_name)

        with allure.step('Клик по борду'):
            self.__driver.find_element(By.CSS_SELECTOR, 'div[id="board"]').click()

    @allure.step('Редактирование карточки') 
    def update_card(self, boardname: str, card_name: str, new_card_name: str) -> None:
        
        self.create_card(boardname, card_name)

        # WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located, (By.CSS_SELECTOR, 'a[data-testid="trello-card"]'))
        WebDriverWait(self.__driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'a[data-testid="trello-card"]'), f'{card_name}'))
        with allure.step('Клик по карточке'):
            
            hidden_element = self.__driver.find_element(By.CSS_SELECTOR, 'a[data-testid="trello-card"]>span')
            while hidden_element.is_displayed() == False:
                #ховер на карточку, чтобы появился карандаш
                hoverable = self.__driver.find_element(By.CSS_SELECTOR, 'a[data-testid="trello-card"]')
                ActionChains(self.__driver).move_to_element(hoverable).perform()
            
                #Клик по карандашику
                WebDriverWait(self.__driver, 10).until(EC.visibility_of, (By.CSS_SELECTOR, 'a[data-testid="trello-card"]>span'))
            
                # state = self.__driver.find_element(By.CSS_SELECTOR, 'a[data-testid="trello-card"]>span').is_displayed()
            
                self.__driver.find_element(By.CSS_SELECTOR, 'a[data-testid="trello-card"]>span').click()

            #Очистка поля и внесение нового названия карточки
            self.__driver.find_element(By.CSS_SELECTOR, 'textarea[class="list-card-edit-title js-edit-card-title"]').clear()
            self.__driver.find_element(By.CSS_SELECTOR, 'textarea[class="list-card-edit-title js-edit-card-title"]').send_keys(new_card_name)
            
            # Клик по "Сохранить"
            self.__driver.find_element(By.CSS_SELECTOR, 'input[value="Сохранить"]').click()

            # hoverable = self.__driver.find_element(By.CSS_SELECTOR, 'a[data-testid="trello-card"]>span')
            # ActionChains(self.__driver).move_to_element(hoverable).perform()
            # hoverable.click()
            # sleep(5)
    
    @allure.step('Удаление карточки') 
    def delete_card(self) -> None:
        # self.create_card()
        
        #ховер на карточку, чтобы появился карандаш
        hoverable = self.__driver.find_element(By.CSS_SELECTOR, 'a[data-testid="trello-card"]')
        ActionChains(self.__driver).move_to_element(hoverable).perform()
        
        #Клик по карандашику
        self.__driver.find_element(By.CSS_SELECTOR, 'a[data-testid="trello-card"]>span').click()
        
        #Клик по "Архивировать"
        self.__driver.find_element(By.CSS_SELECTOR, 'a[data-testid="quick-card-editor-archive"]').click()
    
    @allure.step('Перемещение карточки') 
    def move_card(self) -> None:
        return

    # @allure.step('Перемещение карточки') 
    def get_board_id(self) -> str:
        """
        Получаем id доски из json
        
        Returns:
            str: id доски из json
        """
        board_url = self.__driver.current_url
        self.__driver.get(f'{board_url}.json')
        resp = json.loads(self.__driver.find_element(By.TAG_NAME, 'pre').text)

        return(resp['id'])
    