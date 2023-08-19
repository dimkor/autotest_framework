import pytest
import allure
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver import ActionChains
import json
from selenium.webdriver.common.keys import Keys
from pages.LoginPage import LoginPage
from testdata.DataProvider import DataProvider
import urllib.parse

class MainPage:
    
    url = DataProvider().get('url')
    username = DataProvider().get('username')
    ui_token = DataProvider().get('ui_token')
    
    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver
        self.__driver.get(self.url+f'u/{self.username}/boards')
        
        with allure.step('Устанавливаем куки авторизации'):
            cookie = {
                "name":"token",
                "value": f'{self.ui_token}'
            }
            self.__driver.add_cookie(cookie)
        
        my_try = 0    
        while self.__driver.title.startswith('Ошибка'):
            with allure.step('Открываем рабочее пространство пользователя'):
                self.__driver.get(self.url+f'u/{self.username}/boards')
            #выход из цикла в том случае, если 10 раз нас постигает неудача
            my_try = my_try + 1
            if my_try == 9:
                self.__driver.quit()
                
    @allure.step('Создание доски')   
    def create_board(self, boardname: str) -> str:
        """
        Создание доски
        
        Returns:
            boardname (str): имя доски
        """        
        # with allure.step(''):
        with allure.step('Клик на кнопку "Создать доску"'):
            self.__driver.find_element(By.CSS_SELECTOR, 'div[class="board-tile mod-add"]').click()
        
        with allure.step('Заполнение поля "Заголовок доски"'):
            self.__driver.find_element(By.CSS_SELECTOR, 'input[data-testid="create-board-title-input"]').clear()
            self.__driver.find_element(By.CSS_SELECTOR, 'input[data-testid="create-board-title-input"]').send_keys(boardname)
        
        with allure.step('Клик по кнопке "Создать"'):
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
    def delete_board(self, board: dict) -> None:
        """
        Удаление доски
        
        Returns:
            board (dict): json с информацией о доске
        """           
        self.__driver.get(board['url'])
        
        WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable, (By.CSS_SELECTOR, 'h1[data-testid="board-name-display"]'))
        
        with allure.step('Клик на три точки'):
            WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable, (By.CSS_SELECTOR, 'button[aria-label="Меню"]'))
            self.__driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Меню"]').click()
        
        with allure.step('Клик на "Закрыть доску"'):
            WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable, (By.CSS_SELECTOR, 'ul[class="board-menu-navigation"]>li:last-child'))
            self.__driver.find_element(By.CSS_SELECTOR, 'ul[class="board-menu-navigation"]>li:last-child').click()
        
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
    def create_card(self, board: dict, list: dict, card_name: str, lists: dict) -> None:
        """
        Создание карточки
        
        Args:
            board (dict): json с информацией о доске
            list (dict): json с информацией о списке
            card_name (str): имя карточки
            lists (dict): json с информацией о списках на доске
        """
        self.__driver.get(board['url'])
        
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
    def update_card(self, card: dict, new_card_name: str) -> None:
        """
        Редактирование карточки

        Args:
            card (dict): json с информацией о карточке
            new_card_name (str): новое имя карточки
        """
        self.__driver.get(card['url'])
        
        with allure.step('Клик по карточке'):
            # self.__driver.find_element(By.LINK_TEXT, '{card_name}'.format(card_name=card['name'])).click()
            WebDriverWait(self.__driver, 10).until(EC.visibility_of, (By.CSS_SELECTOR, 'textarea[class="mod-card-back-title js-card-detail-title-input"]'))
            self.__driver.find_element(By.CSS_SELECTOR, 'textarea.js-card-detail-title-input').clear()
            self.__driver.find_element(By.CSS_SELECTOR, 'textarea.js-card-detail-title-input').send_keys(new_card_name)
            self.__driver.find_element(By.CSS_SELECTOR, 'textarea.js-card-detail-title-input').send_keys(Keys.RETURN)

            self.__driver.find_element(By.CSS_SELECTOR, 'a[aria-label="Закрыть диалоговое окно"]').click()

    @allure.step('Удаление карточки') 
    def delete_card(self, board: dict, card: dict) -> None:
        """
        Удаление карточки

        Args:
            board (dict): json c информацией о доске
            card (dict): json c информацией о карточке
        """
        self.__driver.get(card['url'])
        
        with allure.step('Клик по кнопке "Архивация"'):       
            WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located, (By.CSS_SELECTOR, 'a[title="Архивация"]'))
            self.__driver.find_element(By.CSS_SELECTOR, 'a[title="Архивация"]').click()
        
        with allure.step('Клик по кнопке "Удалить"'):       
            WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located, (By.CSS_SELECTOR, 'a[title="Удалить"]'))
            self.__driver.find_element(By.CSS_SELECTOR, 'a[title="Удалить"]').click()
        
        with allure.step('Клик по кнопке "Удалить" в модальном окне'):       
            WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located, (By.CSS_SELECTOR, 'input[value="Удалить"]'))
            self.__driver.find_element(By.CSS_SELECTOR, 'input[value="Удалить"]').click()
        
        with allure.step('Ожидаем, что url изменится'):
            WebDriverWait(self.__driver, 10).until(EC.url_to_be(board['url']))
                
    @allure.step('Перемещение карточки') 
    def move_card(self, board: dict) -> None:
        """
        Перемещение карточки

        Args:
            board (dict): json с информацией о доске
        """
        self.__driver.get(board['url'])
        
        with allure.step('Клик и холд карточки и перенос во второй список'):
            draggable = self.__driver.find_element(By.CSS_SELECTOR, 'a[data-testid="trello-card"]')
            droppable = self.__driver.find_element(By.CSS_SELECTOR, '#board>div:nth-child(2)')
            ActionChains(self.__driver).drag_and_drop(draggable, droppable).perform()
    
    @allure.step('Получить id доски') 
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